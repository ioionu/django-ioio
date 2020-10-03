from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.views.generic.list import ListView
from .models import Post
# Create your views here.

class PostList(ListView):
  paginate_by = 5
  model = Post


def post(request, path):
  post = get_object_or_404(Post, slug=path)
  return render(request, 'blog/post.html', {'post': post})
