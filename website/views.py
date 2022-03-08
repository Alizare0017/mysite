

from django.http import HttpResponse
from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return HttpResponse('<h1>Home page<h1>')

def about(request):
    return HttpResponse('<h1>about<h1>')

def contact(request):
    return HttpResponse('<h1>contact<h1>')