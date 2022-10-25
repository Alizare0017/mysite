from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Post(models.Model):
    # image
    
    author = models.ForeignKey(User,on_delete=models.SET_NULL,null=True)
    title = models.CharField(max_length=255)
    content = models.TextField()
    # tag
    # category
    counted_view = models.IntegerField(default=0)
    status = models.BooleanField(default=False)
    published_date = models.TimeField(null=True)
    created_date = models.TimeField(auto_now_add=True)
    updated_date = models.TimeField(auto_now=True)
    
    def __str__(self):
       return "{} - {}".format(self.title, self.id)
    
    
