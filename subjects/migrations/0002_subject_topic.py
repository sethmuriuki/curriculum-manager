# -*- coding: utf-8 -*-
# Generated by Django 1.11.9 on 2018-05-17 11:36
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('subjects', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='subject',
            name='topic',
            field=models.CharField(max_length=30, null=True),
        ),
    ]
