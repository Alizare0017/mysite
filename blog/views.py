from urllib import request
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse
from blog.models import Post
<<<<<<< Updated upstream

def blog_single(request,pid):
    posts = get_object_or_404(Post,id=pid,status=1)
    context = {'posts' : posts}
=======
from django.shortcuts import get_object_or_404

def blog_single(request,pid):
    posts = Post.objects.filter(id=pid)
    context = {'posts':posts}
>>>>>>> Stashed changes
    return render(request,'blog/blog-single.html',context)

def blog_home(request):
    posts = Post.objects.filter(status=1)
    context = {'posts' : posts}
    return render(request,'blog/blog-home.html',context)
<<<<<<< Updated upstream

def test(request,testID) :
    posts = Post.objects.filter(id=testID)
    context = {'posts' : posts}
    return render(request,'test.html',context)
=======
    
def test(request,test):
    posts = Post.objects.filter(status=1)
    context = {'test': test}
    return render(request, 'test.html', context)
>>>>>>> Stashed changes
