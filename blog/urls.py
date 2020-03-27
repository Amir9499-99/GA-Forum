from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='blog-home'),
    path('about/', views.about, name = "blog-about"),
    path('new/event/',views.create_event, name = "create_event"),
    path('post', views.post_create, name='post_create'),
    path('post/like/<int:post_id>', views.add_like, name='add_like'),
    path('post/dislike/<int:post_id>', views.add_dislike, name='add_dislike'),
    path('post/delete/<int:post_id>', views.post_delete, name='post_delete'),
    path('reply/post/<int:post_id>', views.reply_create, name='reply_create'),
]
