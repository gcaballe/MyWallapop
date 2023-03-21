from django.urls import path
from . import views

# URLConf
urlpatterns = [
    
    path('main_page/', views.main_page),
    #path('product/<int:product_id>/', views.single_product),
    path('product/<int:product_id>/', views.single_product, name='single_product'),
    path('author/<int:author_id>/', views.author, name='author'),

    #login stuff
    path('register/', views.register_form),
    path('register_user/', views.register_user),
    path('login_user/', views.login_user),
    path('logout_user/', views.logout_user),
    path('userpanel/', views.userpanel),
]
