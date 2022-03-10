

from django.http import HttpResponse
from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return render(request,'website/home.html')

def about(request):
    return render(request,'about.html')

def contact(request):
    return render(request,'contact.html')