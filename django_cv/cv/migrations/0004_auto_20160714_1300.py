# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-07-14 13:00
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cv', '0003_person_summary'),
    ]

    operations = [
        migrations.AlterField(
            model_name='person',
            name='website',
            field=models.URLField(verbose_name='Homepage url'),
        ),
    ]
