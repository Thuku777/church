# Generated by Django 3.1.2 on 2020-10-29 12:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('about', '0007_auto_20201029_1534'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='about',
            name='slug',
        ),
    ]
