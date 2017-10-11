# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-09-12 18:00
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('farms', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='farm_info',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('lat', models.DecimalField(decimal_places=6, max_digits=15)),
                ('lon', models.DecimalField(decimal_places=6, max_digits=15)),
                ('area', models.DecimalField(decimal_places=2, max_digits=6)),
                ('house_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='farms.House_hold')),
            ],
        ),
    ]
