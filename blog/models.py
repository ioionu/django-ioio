from django.db import models

# Create your models here.
class Image(models.Model):
    title = models.CharField(max_length=512, blank=True)
    image = models.ImageField(null=True)
    alt = models.CharField(max_length=512, blank=True)

class Post(models.Model):
    title = models.CharField(max_length=512)
    body = models.TextField()
    date = models.DateTimeField('Date Published')
    image = models.ManyToManyField(to=Image)
    def __str__(self):
        return self.title

