# Generated by Django 3.1 on 2020-11-16 15:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_urlsdone_urlsleft'),
    ]

    operations = [
        migrations.DeleteModel(
            name='UrlsDone',
        ),
        migrations.DeleteModel(
            name='UrlsLeft',
        ),
        migrations.RemoveField(
            model_name='post',
            name='html',
        ),
    ]
