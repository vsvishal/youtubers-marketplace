# Generated by Django 3.1.4 on 2020-12-11 06:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('webpages', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='slider',
            old_name='subtitile',
            new_name='subtitle',
        ),
    ]
