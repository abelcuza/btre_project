# Generated by Django 3.0.6 on 2020-06-03 17:40

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contacts', '0003_remove_contact_listing'),
    ]

    operations = [
        migrations.AddField(
            model_name='contact',
            name='contact_date',
            field=models.DateTimeField(blank=True, default=datetime.datetime.now),
        ),
        migrations.AddField(
            model_name='contact',
            name='listing',
            field=models.CharField(default='', max_length=200),
        ),
        migrations.AddField(
            model_name='contact',
            name='listing_id',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='contact',
            name='message',
            field=models.TextField(blank=True, default=''),
        ),
        migrations.AddField(
            model_name='contact',
            name='user_id',
            field=models.IntegerField(blank=True, default=1),
        ),
        migrations.AlterField(
            model_name='contact',
            name='email',
            field=models.EmailField(default='', max_length=50),
        ),
        migrations.AlterField(
            model_name='contact',
            name='name',
            field=models.CharField(default='', max_length=200),
        ),
        migrations.AlterField(
            model_name='contact',
            name='phone',
            field=models.CharField(default='', max_length=20),
        ),
    ]
