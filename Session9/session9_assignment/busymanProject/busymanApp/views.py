from django.shortcuts import render, redirect
from .models import Post
from django.utils import timezone
from datetime import datetime, timedelta

# Create your views here.
def new(request):
    if request.method == 'POST':
        Post.objects.create(
            title = request.POST['title'],
            content = request.POST['content'],
            deadline = request.POST.get('deadline'),
        )
    return render(request, 'new.html')

def home(request):
    posts = Post.objects.all().order_by('deadline')
    now = datetime.now().date()
    for post in posts:
        post.days_left = (post.deadline - now).days
    return render(request, 'home.html', {'posts': posts})


def detail(request, post_pk):
    post = Post.objects.get(pk=post_pk)
    return render(request, 'detail.html', {'post': post})

def update(request, post_pk):
    post = Post.objects.get(pk=post_pk)
    
    if request.method == 'POST':
        Post.objects.filter(pk=post.pk).update(
            title = request.POST['title'],
            content = request.POST['content'],
            deadline = request.POST.get('deadline'),
        )
        return redirect('detail', post_pk)
    return render(request, 'update.html', {'post': post})

def delete(request, post_pk):
    post = Post.objects.get(pk=post_pk)
    post.delete()
    
    return redirect('home')