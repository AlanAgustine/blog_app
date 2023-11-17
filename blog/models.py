from django.db import models

# Create your models here.
class blogModel( models.Model):
    title=models.CharField(default='',max_length=100)
    post=models.CharField(default='',max_length=100)
    user_id=models.CharField(default='',max_length=100)
    profile=models.CharField(default='',max_length=10000)

class userModel( models.Model):
    name=models.CharField(default='',max_length=100)
    email=models.CharField(default='',max_length=100)
    user_id=models.CharField(default='',max_length=100)
    password=models.CharField(default='',max_length=10000)

