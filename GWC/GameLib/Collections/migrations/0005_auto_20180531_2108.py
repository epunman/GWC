# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2018-05-31 21:08
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Collections', '0004_auto_20180531_1955'),
    ]

    operations = [
        migrations.AlterField(
            model_name='person',
            name='AuthUser',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
