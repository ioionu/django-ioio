# Generated by Django 3.1.1 on 2020-09-16 12:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0007_auto_20200915_1222'),
    ]

    operations = [
        migrations.RenameField(
            model_name='attachment',
            old_name='image',
            new_name='data',
        ),
    ]