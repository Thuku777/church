# Generated by Django 3.1.2 on 2020-10-30 23:47

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('ministries', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Name of the upcoming event', max_length=100)),
                ('title', models.CharField(help_text='eg. Conference, Meeting etc', max_length=100)),
                ('description', models.TextField(max_length=1000)),
                ('fee', models.CharField(help_text='If free write free otherwise input the amount', max_length=100)),
                ('location', models.CharField(help_text='Location of the event', max_length=100)),
                ('date', models.CharField(help_text='eg. 20th September 2020 to 30th September 2020', max_length=250)),
                ('time', models.CharField(help_text='eg. 1030hrs to 1400hrs', max_length=250)),
                ('date_posted', models.DateTimeField(default=django.utils.timezone.now)),
                ('ministry', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='ministries.ministry')),
            ],
            options={
                'verbose_name': 'Upcoming Event',
                'verbose_name_plural': 'Upcoming Events',
            },
        ),
    ]
