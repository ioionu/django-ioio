from django.contrib import admin
from import_export import resources
from blog.models import Post

# Register your models here.
from .models import Post, Image, Attachment

admin.site.register(Post)
admin.site.register(Image)
admin.site.register(Attachment)

class PostResource(resources.ModelResource):
  class Meta:
    model = Post