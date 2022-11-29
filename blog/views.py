from urllib import request
from django.http import HttpResponse
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse
from blog.models import Post

def blog_single(request,pid):
    posts = get_object_or_404(Post,id=pid,status=1)
    context = {'posts' : posts}
    return render(request,'blog/blog-single.html',context)

def blog_home(request,**kwargs):
    posts = Post.objects.filter(status=1)
    if kwargs.get('cat_name'):
        posts = posts.filter(category__name=kwargs['cat_name'])
    if kwargs.get('author_username'):
        posts = posts.filter(author__username=kwargs['author_username'])
    if kwargs.get('tag_name'):
        posts = posts.filter(tags__name__in=[kwargs['tag_name']])

    posts = Paginator(posts,2)
    try :
        page_number = request.GET.get('page')
        posts = posts.get_page(page_number)

    except PageNotAnInteger :
        posts = posts.get_page(1)

    except EmptyPage :
        posts = posts.get_page(1)

    context = {'posts' : posts}
    return render(request,'blog/blog-home.html',context)

def test(request) :
    return render(request,'test.html')

def blog_search(request):
    posts = Post.objects.filter(status=1)
    if request.method == 'GET' :
        posts = posts.filter(content__contains=request.GET.get('s'))

    context = {'posts' : posts}
    return render(request,'blog/blog-home.html',context)









def blog_category(request,cat_name):
    posts = Post.objects.filter(status=1)
    posts = posts.filter(category__name=cat_name)
    context = {'posts' : posts}
    return render(request,'blog/blog-home.html',context)