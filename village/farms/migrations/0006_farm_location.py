# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-09-13 08:31
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('farms', '0005_well_observation'),
    ]

    operations = [
        migrations.CreateModel(
            name='farm_location',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sequence_no', models.IntegerField(default=0, max_length=10)),
                ('lat', models.DecimalField(decimal_places=6, max_digits=15)),
                ('lon', models.DecimalField(decimal_places=6, max_digits=15)),
                ('farm_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='farms.farm_info')),
            ],
        ),
    ]
