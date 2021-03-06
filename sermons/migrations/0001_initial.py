# Generated by Django 3.1.2 on 2020-10-30 23:47

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Sermon',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('sermon', models.URLField(help_text='Add the link of the sermon from youtube or facebook')),
                ('created_by', models.CharField(max_length=100)),
                ('date_posted', models.DateTimeField(default=django.utils.timezone.now)),
            ],
            options={
                'verbose_name': 'Sermon',
                'verbose_name_plural': 'Sermons',
                'ordering': ['date_posted'],
            },
        ),
    ]
