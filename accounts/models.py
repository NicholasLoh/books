from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    picture = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)

     
class Inquiry(models.Model):
    userId = item_id = models.IntegerField(default="0")
    sellerEmail = models.CharField(max_length=200 ,default="example@mail.com")
    item = models.CharField(max_length=200)
    item_id = models.IntegerField()
    name = models.CharField(max_length=200)
    email = models.CharField(max_length=200 ,default="example@mail.com")
    message = models.CharField(max_length=200)
    contact = models.CharField(max_length=200)

