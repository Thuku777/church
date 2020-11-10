# Generated by Django 3.1.2 on 2020-11-06 14:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('slug', models.SlugField()),
                ('parent', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='children', to='media.category')),
            ],
            options={
                'verbose_name': 'Photo Category',
                'verbose_name_plural': 'Photo Categories',
                'unique_together': {('slug', 'parent')},
            },
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=120)),
                ('content', models.TextField(verbose_name='Content')),
                ('created_by', models.CharField(max_length=100)),
                ('draft', models.BooleanField(default=False)),
                ('publish', models.DateField()),
                ('slug', models.SlugField(unique=True)),
                ('category', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='media.category')),
            ],
        ),
    ]
