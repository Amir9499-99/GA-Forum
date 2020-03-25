from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='blog-home'),
    path('about/', views.about, name = "blog-about"),
    path('post', views.post_create, name='post_create'),
    path('post/delete/<int:post_id>', views.post_delete, name='post_delete'),
    path('reply/post/<int:post_id>', views.reply_create, name='reply_create'),
]
