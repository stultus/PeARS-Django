# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-10-18 14:25
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('search', '0002_openvector'),
    ]

    operations = [
        migrations.AddField(
            model_name='openvector',
            name='entropy',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='openvector', to='search.Entropy'),
        ),
    ]