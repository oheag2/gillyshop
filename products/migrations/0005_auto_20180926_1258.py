# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-09-26 12:58
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0004_product_path'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='path',
            field=models.URLField(default=''),
        ),
    ]
