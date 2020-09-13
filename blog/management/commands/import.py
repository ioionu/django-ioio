from django.core.management.base import BaseCommand
from django.utils import timezone
import urllib3
from blog.models import Post, Image, Attachment, Tag
import json
from tablib import Dataset
from blog.admin import PostResource


def get_or_create_tags(tags):
    return [
        Tag.objects.get_or_create(
            title=tag['title']
        )[0]
        for tag in tags
    ]


class Command(BaseCommand):
    help = "I am command derp"

    def handle(self, *args, **kwargs):
        time = timezone.now().strftime('%X')
        self.stdout.write("it is now %s".format(time))

        http = urllib3.PoolManager()
        request = http.request("GET", "http://ioio.test/api/export")
        data = request.data.decode('utf-8')
        posts = json.loads(data)

        for post in posts:
            tags = get_or_create_tags(post['tags'])
            p = Post(
                title=post['title'],
                body=post['body'],
                date=post['created'],
            )
            p.save()
            p.tags.set([tag.id for tag in tags])
            p.save()


        # data_set = Dataset()
        # import_data = data_set.load(request.data)
        