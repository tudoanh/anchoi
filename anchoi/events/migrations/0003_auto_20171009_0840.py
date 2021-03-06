# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-10-09 08:40
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0002_auto_20171009_0401'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='latitude',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='event',
            name='longitude',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='event',
            name='start_time',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
