# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2018-11-16 18:25
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('django_project', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='wish',
            name='granted',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]