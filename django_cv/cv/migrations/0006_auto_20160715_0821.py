# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-07-15 08:21
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cv', '0005_person_photo'),
    ]

    operations = [
        migrations.CreateModel(
            name='Education',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('institution', models.CharField(max_length=60)),
                ('institution_website', models.URLField(max_length=60)),
                ('faculty', models.CharField(max_length=140)),
                ('fromtime', models.DateField()),
                ('totime', models.DateField()),
                ('description', models.TextField()),
                ('ref', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='edu', to='cv.Person')),
            ],
        ),
        migrations.CreateModel(
            name='KeySkills',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('skill', models.CharField(max_length=200)),
                ('ref', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='skills', to='cv.Person')),
            ],
        ),
        migrations.AlterField(
            model_name='experience',
            name='ref',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='work', to='cv.Person'),
        ),
    ]