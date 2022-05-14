from django.db import models

# Create your models here.

class Contact(models.Model):
    name = models.CharField(max_length=255)
    subject = models.CharField(max_length=255)
    massage = models.TextField()
    email = models.EmailField()
    updated_date = models.TimeField(auto_now=True )
    created_date = models.TimeField(auto_now_add=True)