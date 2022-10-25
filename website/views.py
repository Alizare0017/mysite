from urllib import request
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from website.models import *
from blog.models import Post

def index(request):
    return render(request,'website/index.html')

def about(request):
    return render(request,'website/about.html')

def contact(request):
    return render(request,'website/contact.html')

def elements(request):
    return render(request,'website/elements.html')
