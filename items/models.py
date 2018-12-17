from django.db import models
from django.forms import ModelForm
from django.contrib.auth.models import User
from accounts.models import  Profile
from datetime import datetime
# Create your models here.

STREAM_CHOICES = (
    ('all', '全部'),
    ('理科', '理科'),
    ('文商', '文商科'),
    ('商', '商科'),
    ('商文商', '商文商'),
)
class Item(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    picture = models.ManyToManyField(Profile)
    title = models.CharField(max_length=200)
    description = models.CharField(max_length=200)
    stream = models.CharField(max_length=5,  choices=STREAM_CHOICES)
    price = models.CharField(max_length=200)
    is_sold = models.BooleanField(default=False)
    photo_main = models.ImageField(upload_to='photos/%Y/%m/%d/')
    photo_1 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    photo_2 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    photo_3 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    photo_4 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    photo_5 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    photo_6 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    list_date = models.DateTimeField(default=datetime.now, blank=True)
    def __str__(self):
        return self.title
