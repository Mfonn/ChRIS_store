# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2018-02-15 21:12
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import plugins.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Plugin',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('creation_date', models.DateTimeField(auto_now_add=True)),
                ('modification_date', models.DateTimeField(auto_now_add=True)),
                ('name', models.CharField(max_length=100, unique=True)),
                ('dock_image', models.CharField(max_length=500)),
                ('public_repo', models.URLField(max_length=300)),
                ('descriptor_file', models.FileField(max_length=512, upload_to=plugins.models.uploaded_file_path)),
                ('type', models.CharField(choices=[('ds', 'Data plugin'), ('fs', 'Filesystem plugin')], default='ds', max_length=4)),
                ('authors', models.CharField(blank=True, max_length=200)),
                ('title', models.CharField(blank=True, max_length=400)),
                ('category', models.CharField(blank=True, max_length=100)),
                ('description', models.CharField(blank=True, max_length=800)),
                ('documentation', models.CharField(blank=True, max_length=800)),
                ('license', models.CharField(blank=True, max_length=50)),
                ('version', models.CharField(blank=True, max_length=10)),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='plugins', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ('type',),
            },
        ),
        migrations.CreateModel(
            name='PluginParameter',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('optional', models.BooleanField(default=True)),
                ('default', models.CharField(blank=True, max_length=200)),
                ('type', models.CharField(choices=[('string', 'String values'), ('float', 'Float values'), ('boolean', 'Boolean values'), ('integer', 'Integer values'), ('path', 'Path values')], default='string', max_length=10)),
                ('help', models.TextField(blank=True)),
                ('plugin', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='parameters', to='plugins.Plugin')),
            ],
            options={
                'ordering': ('plugin',),
            },
        ),
    ]
