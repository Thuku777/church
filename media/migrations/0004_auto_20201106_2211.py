# Generated by Django 3.1.2 on 2020-11-06 19:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('media', '0003_auto_20201106_2146'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='category',
            name='photo',
        ),
        migrations.AlterField(
            model_name='photo',
            name='category',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='media.category'),
        ),
    ]
