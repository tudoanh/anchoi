# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-11-13 10:33
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0006_auto_20171105_1004'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='facebookpage',
            name='name',
        ),
    ]
