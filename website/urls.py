
from turtle import home
from unicodedata import name
from django.urls import path
from website.views import *

app_name = 'website'

urlpatterns = [
    path('',index,name='index'),
    path('contact',contact,name='contact'),
    path('about',about,name='about'),
    path('elements',elements,name='elements'),
    #path('<str:pid>',test,name='test'),
] 
