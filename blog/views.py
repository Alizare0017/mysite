from urllib import request
from django.http import HttpResponse
from django.shortcuts import render
from django.http import HttpResponse

def blog_single(request):
    return render(request,'blog/blog-single.html')

def blog_home(request):
    return render(request,'blog/blog-home.html')