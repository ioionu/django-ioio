from django.urls import path

from . import views

app_name = 'blog'

urlpatterns = [
  path('', views.index, name='index'),
  path('<path:path>', views.post, name='post')
]
