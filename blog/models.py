from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from PIL import Image
from django import forms
from datetime import date






class Post(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    strContent = models.TextField()
    date = models.DateTimeField(default=timezone.now)
    num_likes = models.IntegerField(default=0)
    num_dislikes = models.IntegerField(default=0)

    def __str__(self):
        return f'{self.author} said: {self.strContent} on {self.date}\n'

class Reply(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    strContent = models.TextField()
    date = models.DateTimeField(default=timezone.now)
    num_likes = models.IntegerField(default=0)
    
    def __str__(self):
        return f'{self.author} Replied to {self.post.author}: {self.strContent} on {self.date}\n'






class Event(models.Model):
    host = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateField(default=timezone.now)
    location = models.CharField(max_length=150,default='over zoom :(')
    name = models.CharField(max_length=150,default='Party Time!!!')
    description = models.CharField(max_length=300,default='very fun time')
    num_attendees = models.IntegerField(default=0)
    num_nopes = models.IntegerField(default=0)
    photo = models.ImageField(default='profile_pics/cake.png',upload_to='profile_pics')


