# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-10-10 12:29
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0004_auto_20171009_0909'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='latitude',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='event',
            name='longitude',
            field=models.FloatField(blank=True, null=True),
        ),
    ]
