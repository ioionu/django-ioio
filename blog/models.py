from django.db import models

class Image(models.Model):
    title = models.CharField(max_length=512, blank=True, null=True)
    image = models.ImageField(null=True)
    alt = models.CharField(max_length=512, blank=True, null=True)


class Attachment(models.Model):
    title = models.CharField(max_length=512, blank=True)
    data = models.FileField(blank=True)


class Tag(models.Model):
    title = models.CharField(max_length=512, blank=True)

    def __str__(self):
        return self.title


class Post(models.Model):
    title = models.CharField(max_length=512)
    body = models.TextField()
    date = models.DateTimeField('Date Published')
    image = models.ManyToManyField(to=Image, blank=True)
    attachment = models.ManyToManyField(to=Attachment)
    tags = models.ManyToManyField(to=Tag)
    slug = models.CharField(max_length=512, blank=True)

    def __str__(self):
        return self.title

