from django.shortcuts import render
from django.http import HttpResponse
from .models import *

#First hello function
def say_hello(request):
    return render(request, 'hello.html', {'name': 'Guillem'})


#action return template de product
def single_product(request, product_id):

    
    product = Product.objects.get( id=product_id )

    return render(request, 'product-single.html', { 'product': product })


def main_page(request):

    products = Product.objects.all()

    return render(request, 'main.html', { 'products': products} )
    
def author(request, author_id):

    author = User.objects.get(id = author_id)

    return render(request, 'author.html', { 'author': author} )