# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-10-07 04:12
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('farms', '0011_auto_20171006_1823'),
    ]

    operations = [
        migrations.CreateModel(
            name='crops',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('crop', models.CharField(choices=[('cotton', 'cotton'), ('groundnut', 'groundnut'), ('maize', 'maize'), ('paddy', 'paddy'), ('plain', 'plain'), ('sugarcane', 'sugarcane'), ('turmeric', 'turmeric')], default='paddy', max_length=20)),
                ('crop_area', models.IntegerField(default=0)),
            ],
        ),
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
        migrations.AlterField(
            model_name='season_info',
            name='crop',
            field=models.CharField(choices=[('cotton', 'cotton'), ('groundnut', 'groundnut'), ('maize', 'maize'), ('paddy', 'paddy'), ('plain', 'plain'), ('sugarcane', 'sugarcane'), ('turmeric', 'turmeric')], default='paddy', max_length=20),
        ),
        migrations.AddField(
            model_name='crops',
            name='farm_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='farms.farm_info'),
        ),
    ]
