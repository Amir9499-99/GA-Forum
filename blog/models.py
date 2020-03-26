from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from PIL import Image




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
    host = models.OneToOneField(User, on_delete=models.CASCADE)
    picture = models.ImageField(default='profile_pics/unknown.png',upload_to='profile_pics')
    date = models.DateTimeField(default=timezone.now)
    location = models.CharField(max_length=100)

