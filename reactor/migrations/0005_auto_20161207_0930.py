# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-12-07 09:30
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('reactor', '0004_laminations_lam_size'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Laminations',
            new_name='Lamination',
        ),
    ]
