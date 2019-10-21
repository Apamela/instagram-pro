# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-10-21 06:23
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('instagram', '0006_profile_profile_avatar'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='image',
            name='profile_pic',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='profile_avatar',
        ),
        migrations.AddField(
            model_name='image',
            name='post',
            field=models.TextField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='image',
            name='image_comment',
            field=models.ManyToManyField(blank=True, default=False, related_name='comment', to='instagram.Profile'),
        ),
    ]
