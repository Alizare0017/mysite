from django import template
from blog.models import Post, Category

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

@register.inclusion_tag('blog/blog_category.html')
def postcategories():
    posts = Post.objects.filter(status=1)
    category = Category.objects.all()
    cat_dict = {}

    for name in category :
        cat_dict[name]=posts.filter(category=name).count()

    return {'categories' : cat_dict}