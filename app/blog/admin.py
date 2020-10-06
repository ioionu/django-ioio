from django.contrib import admin
from blog.models import Post

# Register your models here.
from .models import Post, Image, Attachment


class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'date')
    # date.admin_order_field('admin')

admin.site.register(Post, PostAdmin)
admin.site.register(Image)
admin.site.register(Attachment)
