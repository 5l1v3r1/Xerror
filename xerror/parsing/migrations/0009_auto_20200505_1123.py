# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2020-05-05 11:23
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('parsing', '0008_exploiated_system_exploit_type'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='exploiated_system',
            name='exploit_type',
        ),
        migrations.AddField(
            model_name='exploiated_system',
            name='exploit_uuid',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='exploiated_system',
            name='exploited',
            field=models.CharField(default=b'no', max_length=255),
        ),
        migrations.AddField(
            model_name='exploiated_system',
            name='session_type',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='exploiated_system',
            name='tunnel_peer',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='exploiated_system',
            name='session_id',
            field=models.CharField(default=b'no', max_length=255),
        ),
    ]
