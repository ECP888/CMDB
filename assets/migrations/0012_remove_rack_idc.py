# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-03-17 10:31
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('assets', '0011_rack_cabinet'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='rack',
            name='idc',
        ),
    ]
