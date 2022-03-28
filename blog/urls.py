from turtle import home
from unicodedata import name
from django.urls import path
from blog.views import *


app_name = 'blog'

urlpatterns = [
    path('blog-single',blog_single,name='blog-single'),
    path('blog-home',blog_home,name='blog-home')
] 