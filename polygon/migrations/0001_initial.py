# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-06-24 18:07
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Provider',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('name', models.CharField(max_length=256)),
                ('email', models.EmailField(db_index=True, max_length=256, unique=True)),
                ('phone_number', models.CharField(max_length=32, unique=True)),
                ('language', models.CharField(max_length=8)),
                ('currency', models.CharField(max_length=8)),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
            },
        ),
        migrations.CreateModel(
            name='Area',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=256)),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('provider', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='areas', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'area',
                'verbose_name_plural': 'areas',
            },
        ),
    ]
