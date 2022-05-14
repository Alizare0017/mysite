from django.db import models

# Create your models here.

class Post(models.Model):
    # image
    
    # author
    
    title = models.CharField(max_length=255)
    content = models.TextField()
    # tag
    # category
    counted_view = models.IntegerField(default=0)
    status = models.BooleanField(default=False)
    published_date = models.TimeField(null=True)
    created_date = models.TimeField(auto_now_add=True)
    updated_date = models.TimeField(auto_now=True)