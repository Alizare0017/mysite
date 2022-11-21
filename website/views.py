from django.shortcuts import render, HttpResponseRedirect
from blog.models import Post
from website.models import *
from website.models import Contact, Newsletter
from website.forms import NameForm, ContactForm, NewsletterForm

def index(request):
    posts = Post.objects.filter(status=1).order_by('created_date')[:3]
    context = {'posts':posts}
    return render(request,'website/index.html',context)


def about(request):
    return render(request,'website/about.html')


def contact(request):
    if request.method == "POST" :
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
    form = ContactForm()
    return render(request,'website/contact.html',{'form':form})

def elements(request):
    return render(request,'website/elements.html')


def newsletter_view(request):
    print('wtf')
    if request.method == "POST" :
        form = NewsletterForm(request.POST)
        print('here')
        if form.is_valid():
            print('fds')
            form.save()
            
    return HttpResponseRedirect('/')