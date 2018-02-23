# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-02-22 07:49
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='crud',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('course_name', models.CharField(max_length=255)),
                ('description', models.CharField(max_length=255)),
                ('created_At', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name_plural': 'crud',
            },
        ),
    ]