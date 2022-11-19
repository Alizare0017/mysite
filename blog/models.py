from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

        
class Post(models.Model):
    image = models.ImageField(upload_to='blog/',default='blog/default.jpg')
    author = models.ForeignKey(User,on_delete=models.SET_NULL,null=True)

    title = models.CharField(max_length=255)
    content = models.TextField()
    # tag
    category = models.ManyToManyField(Category)
    counted_view = models.IntegerField(default=0)
    status = models.BooleanField(default=False)
    created_date = models.DateTimeField(auto_now=True,null=True)
    updated_date = models.TimeField(auto_now=True)
    class Meta :
        ordering = ['id']

    def __str__(self):
       return "{} - {}".format(self.title, self.pk)
    
    def snippest(self):
        return self.content[:100] + ' . . .'
    
