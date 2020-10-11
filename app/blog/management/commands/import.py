from django.core.management.base import BaseCommand
from django.core.files import File
from django.utils import timezone
import urllib3
import urllib
from blog.models import Post, Image, Attachment, Tag
import json
from tablib import Dataset
import os


LOCAL_IMG_DIR = os.environ.get("LOCAL_IMG_DIR")
LOCAL_ATTACHMENT_DIR = os.environ.get("LOCAL_ATTACHMENT_DIR")

def get_or_create_tags(tags):
    return [
        Tag.objects.get_or_create(
            title=tag['title']
        )[0]
        for tag in tags
    ]

def get_or_create_images(images):
    imageObjects = []
    for image in images:
        title = image['title'] if 'title' in image else None
        filename = urllib.parse.unquote(image['url'].split("/")[-1])
        local_path = LOCAL_IMG_DIR + "/" + filename

        img = Image(title=title, alt=image['alt'])
        img.image.save(filename, File(open(local_path, 'rb')))
        imageObjects.append(img)
    return imageObjects

def get_or_create_file(files):
    fileObjects = []
    for f in files:
        filename = urllib.parse.unquote(f['url'].split("/")[-1])
        local_path = LOCAL_ATTACHMENT_DIR + "/" + filename
        attachment = Attachment(title=f['description'])
        attachment.data.save(filename, File(open(local_path, 'rb')))
        fileObjects.append(attachment)
    return fileObjects

class Command(BaseCommand):
    help = "I am command derp"

    def handle(self, *args, **kwargs):
        time = timezone.now().strftime('%X')
        self.stdout.write("it is now %s".format(time))

        Post.objects.all().delete()
        Image.objects.all().delete()
        Attachment.objects.all().delete()

        http = urllib3.PoolManager()
        request = http.request("GET", "http://10.20.1.2/api/export", headers={'Host': 'ioio.test'})
        data = request.data.decode('utf-8')
        posts = json.loads(data)

        for post in posts:
            tags = get_or_create_tags(post['tags'])
            images = get_or_create_images(post['images'])
            attachments = get_or_create_file(post['attachments'])
            p = Post(
                title=post['title'],
                body=post['body'],
                date=post['created'],
                slug=post['slug'][1:]
            )
            p.save()
            p.tags.set([tag.id for tag in tags])
            p.image.set([image.id for image in images])
            p.attachment.set([attachment.id for attachment in attachments])
            p.save()


        # data_set = Dataset()
        # import_data = data_set.load(request.data)
        