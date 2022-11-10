from urllib import request
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse
from blog.models import Post

def blog_single(request,pid):
    posts = get_object_or_404(Post,id=pid,status=1)
    context = {'posts' : posts}
    return render(request,'blog/blog-single.html',context)

def blog_home(request):
    posts = Post.objects.filter(status=1)
    context = {'posts' : posts}
    return render(request,'blog/blog-home.html',context)

def test(request) :
    return render(request,'test.html')
