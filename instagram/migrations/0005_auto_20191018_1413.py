# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-10-18 12:13
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('instagram', '0004_delete_post'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comments',
            name='author',
        ),
        migrations.DeleteModel(
            name='comments',
        ),
    ]