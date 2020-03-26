from django.contrib import admin
from .models import Post
from .models import Reply
from .models import Event
admin.site.register(Post)
admin.site.register(Reply)
admin.site.register(Event)
# Register your models here.
