# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-10-17 21:47
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0010_product_imagetwo'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='url',
        ),
    ]
