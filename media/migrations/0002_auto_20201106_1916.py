# Generated by Django 3.1.2 on 2020-11-06 16:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('media', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='post',
            options={'verbose_name': 'Photo Gallery', 'verbose_name_plural': 'Photo Gallery'},
        ),
        migrations.AddField(
            model_name='post',
            name='photo',
            field=models.ImageField(blank=True, null=True, upload_to='images/media_team/%Y/%m/%d/'),
        ),
    ]
