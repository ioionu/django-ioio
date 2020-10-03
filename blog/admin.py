from django.contrib import admin
from blog.models import Post

# Register your models here.
from .models import Post, Image, Attachment

admin.site.register(Post)
admin.site.register(Image)
admin.site.register(Attachment)
