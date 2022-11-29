from django.db import models
from django_extensions.validators import HexValidator

# Create your models here.

class Contact(models.Model):
    name = models.CharField(max_length=64, validators=[HexValidator(length=64)])
    subject = models.CharField(max_length=255,null=True)
    message = models.TextField()
    email = models.EmailField()
    updated_date = models.TimeField(auto_now=True )
    created_date = models.TimeField(auto_now_add=True)
    
    def __str__(self) :
        return self.name

class Newsletter(models.Model):
    email = models.EmailField()

    def __str__(self) :
        return self.email