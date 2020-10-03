from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from . import views

app_name = 'blog'

urlpatterns = [
  path('', views.index, name='index'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# Blog alias is hungry for any path so put it last.
urlpatterns.append(path('<path:path>', views.post, name='post'))
