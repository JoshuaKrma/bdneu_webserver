# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-06-27 08:23
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('webapp1', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='msgpost',
            options={'ordering': ['-datetime']},
        ),
    ]
