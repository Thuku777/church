# Generated by Django 3.1.2 on 2020-10-31 12:42

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Header',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slide_1', models.ImageField(null=True, upload_to='images/Slides/%Y/%m/%d/')),
                ('slide_2', models.ImageField(null=True, upload_to='images/Slides/%Y/%m/%d/')),
                ('slide_3', models.ImageField(null=True, upload_to='images/Slides/%Y/%m/%d/')),
                ('is_published', models.BooleanField(default=True)),
            ],
        ),
    ]