from django.urls import path
from . import views

# URLConf
urlpatterns = [
    path('hello/', views.say_hello),
    path('main_page/', views.main_page),
    #path('product/<int:product_id>/', views.single_product),
    path('product/<int:product_id>/', views.single_product, name='single_product'),
    path('author/<int:author_id>/', views.author, name='author')
]