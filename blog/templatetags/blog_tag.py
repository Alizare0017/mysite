from django import template
from blog.models import Post

register = template.Library()

@register.simple_tag(name='posts')
def function() :
    posts = Post.objects.filter(status=1)
    return posts

@register.filter
def snippet(value, fl):
    return value[:fl]

@register.inclusion_tag('blog/blog_latest_posts.html')
def latestposts():
    posts = Post.objects.filter(status=1).order_by("created_date")
    return {'posts' : posts}