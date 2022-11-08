from turtle import home
from unicodedata import name
from django.urls import path
from blog.views import *
<<<<<<< Updated upstream
from django.conf import settings
from django.conf.urls.static import static
=======
>>>>>>> Stashed changes

app_name = 'blog'

urlpatterns = [
<<<<<<< Updated upstream
    path('blog/<int:pid>',blog_single,name='blog-single'),
    path('blog-home',blog_home,name='blog-home'),
    path('test/<str:testID>',test,name='test'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
=======
    path('post/<int:pid>',blog_single,name='blog-single'),
    path('blog-home',blog_home,name='blog-home'),
    path('test/<str:test>', test, name='test'),
]
>>>>>>> Stashed changes
