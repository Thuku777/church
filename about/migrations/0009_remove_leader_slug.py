# Generated by Django 3.1.2 on 2020-10-29 12:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('about', '0008_remove_about_slug'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='leader',
            name='slug',
        ),
    ]