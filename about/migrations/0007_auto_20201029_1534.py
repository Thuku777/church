# Generated by Django 3.1.2 on 2020-10-29 12:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('about', '0006_auto_20201027_2057'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='about',
            options={'ordering': ['-id'], 'verbose_name': 'About', 'verbose_name_plural': 'About'},
        ),
    ]
