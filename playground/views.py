from django.shortcuts import render
from django.http import HttpResponse
from .models import *

#action return template de product
def single_product(request, product_id):

    
    product = Product.objects.get( id=product_id )

    return render(request, 'product-single.html',{ 'product': product })


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

    return render(request, 'author.html', { 'author': author } )

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

        u = request.POST.get("username")
        p = request.POST.get("psw")

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

    return render(request, 'userpanel.html', {'user': user, 'usersession': u})
