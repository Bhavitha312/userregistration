from django.db import models

# Create your models here.
class user(models.Model):
    name=models.CharField(null=False,max_length=50)
    lastname=models.CharField(null=False,max_length=50)
    password=models.CharField(null=False,max_length=50)