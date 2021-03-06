# Generated by Django 3.1.1 on 2020-09-13 11:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_auto_20200913_0325'),
    ]

    operations = [
        migrations.CreateModel(
            name='Attachment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=512)),
                ('image', models.FileField(blank=True, upload_to='')),
            ],
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=512)),
            ],
        ),
        migrations.AddField(
            model_name='post',
            name='slug',
            field=models.CharField(blank=True, max_length=512),
        ),
        migrations.AlterField(
            model_name='post',
            name='image',
            field=models.ManyToManyField(blank=True, to='blog.Image'),
        ),
        migrations.AddField(
            model_name='post',
            name='attachment',
            field=models.ManyToManyField(to='blog.Attachment'),
        ),
    ]
