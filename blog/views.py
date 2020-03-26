from django.shortcuts import render, redirect
from .models import Post
from .models import Reply
from .models import Event
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import EventCreationForm


# Create your views here.



def home(request):

    event_creation_form = EventCreationForm()

    context = {
        'posts':reversed(Post.objects.all()),
        'event_creation_form': event_creation_form,
        'events':Event.objects.all(),
    }
    return render(request,'blog/home.html',context)

def about(request):
    return render(request,'blog/about.html')

@login_required
def post_create(request):
    post = Post( author = request.user, strContent = request.POST.get('post-input') )
    print(post)
    post.save()
    next = request.POST.get('currentpath', '/')
    return redirect(next)

@login_required
def reply_create(request, post_id):
    post = Post.objects.get(id = post_id)
    reply = Reply( author = request.user, post = post, strContent = request.POST.get('input-comment') )
    reply.save()
    next = request.POST.get('currentpath', '/')
    return redirect(next)


def post_delete(request,post_id):
    Post.objects.filter(id=post_id).delete()
    next = request.POST.get('currentpath', '/')
    return redirect(next)
     

def add_like(request,post_id):
    post_to_like = Post.objects.filter(id=post_id)[0]
    print('this is the post',post_to_like)
    post_to_like.num_likes += 1
    post_to_like.save()
    next = request.POST.get('currentpath', '/')
    return redirect(next)
     

def add_dislike(request,post_id):
    post_to_dislike = Post.objects.filter(id=post_id)[0]
    post_to_dislike.num_dislikes += 1
    post_to_dislike.save()
    next = request.POST.get('currentpath', '/')
    return redirect(next)
     
