from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Post
# Create your views here.

def index(request):
  Post.objects.all().count()
  return HttpResponse("hello derp")


def post(request, path):
  post = get_object_or_404(Post, slug=path)
  return HttpResponse("hello {path}".format(path=path))
