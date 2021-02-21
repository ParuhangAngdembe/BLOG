from django.contrib import admin
from django.urls import path
from .views import *


urlpatterns = [
    path('', index, name='home'),
    path('about', about, name='about' ),
    path('services', services, name='services'),
    path('portfolio',portfolio, name= 'portfolio'),
    path('price', price, name='price'),
    path('contact', contact, name="contact"),
    path('blog-home', blogHome, name="blogHome"),
    path('blog-single', blogSingle, name="blog-single"),
    path('elements', elements, name="elements"),
]
