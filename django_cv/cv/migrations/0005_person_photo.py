# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-07-14 13:31
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('cv', '0004_auto_20160714_1300'),
    ]

    operations = [
        migrations.AddField(
            model_name='person',
            name='photo',
            field=models.ImageField(default=datetime.datetime(2016, 7, 14, 13, 31, 30, 296286, tzinfo=utc), upload_to='/media/'),
            preserve_default=False,
        ),
    ]
