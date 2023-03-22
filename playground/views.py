from django.shortcuts import render
from django.http import HttpResponse
from django.core.files.storage import FileSystemStorage
from .models import *
from django.conf import settings


#action return template de product
def single_product(request, product_id):

    
    product = Product.objects.get( id=product_id )
    comments = Comment.objects.filter(product=product_id)
    usersession = request.session.get('usersession','')

    return render(request, 'product-single.html',
                { 
                    'product': product ,
                    'comments': comments,
                    'usersession': usersession,
                })


def main_page(request):

    products = Product.objects.all()

    for p in products:
        num_comments = len(p.getComments())
        comments = p.getComments()
        p = p.__dict__
        p['comments_len'] = num_comments
        p['comments'] = comments

    usersession = request.session.get('usersession','')

    return render(request, 'main.html', { 'products': products, 'usersession': usersession} )
    
def author(request, author_id):

    author = User.objects.get(id = author_id)
    usersession = request.session.get('usersession','')

    products = Product.objects.filter(author=author).all()
    plen = len(products)
    for p in products:
        num_comments = len(p.getComments())
        comments = p.getComments()
        p = p.__dict__
        p['comments_len'] = num_comments
        p['comments'] = comments

    return render(request, 'author.html',
            {
            'author': author, 'plen': plen ,
            'products': products,
            'usersession': usersession
            }
    )

def register_form(request):

    return render(request, 'register_form.html')

def register_user(request):

    if request.method == 'POST':

        u = request.POST.get("username")

        newUser = User(
            username=u,
            password=request.POST.get("psw"),
        )
        newUser.save(newUser)

        request.session['usersession'] = u

    #enllaço amb main page
    return main_page(request)

def login_user(request):

    if request.method == 'POST':

        u = request.POST.get("login_username")
        p = request.POST.get("login_psw")

        if User.objects.filter(username=u,password=p).exists():
            print('logged')
            request.session['usersession'] = u

    #TO-DO return error NO LOGIN

    #enllaço amb main page
    return main_page(request)

def logout_user(request):

    request.session.flush()
    return main_page(request)

def userpanel(request):

    u = request.session['usersession']
    user = User.objects.get(username=u)
    products = Product.objects.filter(author=user).all()

    return render(request, 'userpanel.html',
                {
                    'user': user,
                    'usersession': u, #fa falta per el navbar
                    'products': products
                })



#inserrir un comentari
def insert_comment(request):

    if request.method == 'POST':

        t = request.POST.get("comment_text")
        u = request.POST.get("comment_author_username")
        p = request.POST.get("comment_product")

        user = User.objects.get(username=u)
        prod= Product.objects.get(id=p)

        newComment = Comment(
            author=user,
            product=prod,
            text=t,
        )
        newComment.save(newComment)

    #enllaço amb main page
    return single_product(request, p)



def modify_userinfo(request):

    if request.method == 'POST':

        p = request.POST.get("inputPassword")
        d = request.POST.get("inputDescripcion")
        c = request.POST.get("inputCity")
        a = request.POST.get("inputAvatar")

        u = request.session['usersession']

        image_file  = request.FILES['inputAvatar']


        fs = FileSystemStorage()
        filename = fs.save(image_file.name, image_file)
        uploaded_file_url = fs.url(filename)
       
       
        user = User.objects.get(username=u)
        user.password = p
        user.description = d
        user.city = c
        
        user.avatar = image_file.name

        user.save()


    return userpanel(request)


def modify_product(request):

    u = request.session['usersession']
    user = User.objects.get(username=u)

    if request.method == 'POST':

        n = request.POST.get("inputNombre")
        p = request.POST.get("inputPrice")
        d = request.POST.get("inputDescripcionProd")
        i = request.POST.get("inputImagen")


        idProd = request.POST.get("idProduct")
        uon = request.POST.get("updateOrNew")

        if uon == 'new':
            image_file  = request.FILES['inputImagen']
            fs = FileSystemStorage()
            filename = fs.save(image_file.name, image_file)
            uploaded_file_url = fs.url(filename)

        print(uon)

        if uon == 'new':

            newProduct = Product(
                name = n,
                price = p,
                description = d,
                image = image_file.name,
                author=user
                
            )
            newProduct.save(newProduct)

        elif uon == 'update':

            existingProduct = Product.objects.get(id=idProd)
            existingProduct.name = n
            existingProduct.price = p
            existingProduct.description = d

            if i != None:
                image_file  = request.FILES['inputImagen']
                fs = FileSystemStorage()
                filename = fs.save(image_file.name, image_file)
                uploaded_file_url = fs.url(filename)
                existingProduct.image = image_file.name

            existingProduct.save()
        
        else:
            #cas DELETE
            print('deleting the product:')
            print(idProd)
            Product.objects.filter(id=idProd).delete()



    return userpanel(request)