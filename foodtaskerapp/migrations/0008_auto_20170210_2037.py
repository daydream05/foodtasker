# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-02-10 20:37
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('foodtaskerapp', '0007_auto_20170210_2036'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orderdetail',
            name='order',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='order_detail', to='foodtaskerapp.Order'),
        ),
    ]
