# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-09-13 12:06
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('farms', '0008_auto_20170913_0850'),
    ]

    operations = [
        migrations.AlterField(
            model_name='farm_info',
            name='house_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='farms.house_hold'),
        ),
        migrations.AlterField(
            model_name='persons_info',
            name='house_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='farms.house_hold'),
        ),
    ]
