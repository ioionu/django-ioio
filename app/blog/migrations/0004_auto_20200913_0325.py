# Generated by Django 3.1.1 on 2020-09-13 03:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_post_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=512)),
                ('image', models.ImageField(null=True, upload_to='')),
                ('alt', models.CharField(blank=True, max_length=512)),
            ],
        ),
        migrations.RemoveField(
            model_name='post',
            name='image',
        ),
        migrations.AddField(
            model_name='post',
            name='image',
            field=models.ManyToManyField(to='blog.Image'),
        ),
    ]
