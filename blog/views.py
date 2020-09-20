from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Post
# Create your views here.

def index(request):
  posts = Post.objects.all()
  return render(request, 'blog/index.html', {'posts': posts})


def post(request, path):
  post = get_object_or_404(Post, slug=path)
  return render(request, 'blog/post.html', {'post': post})
