# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-09-26 18:53
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0007_delete_urlfield'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='path',
            new_name='url',
        ),
    ]
