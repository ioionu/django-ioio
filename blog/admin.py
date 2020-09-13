from django.contrib import admin
from import_export import resources
from blog.models import Post

# Register your models here.
from .models import Post, Image

admin.site.register(Post)
admin.site.register(Image)

class PostResource(resources.ModelResource):
  class Meta:
    model = Post