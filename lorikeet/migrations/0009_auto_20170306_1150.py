# -*- coding: utf-8 -*-
# Generated by Django 1.9.9 on 2017-03-06 01:20
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lorikeet', '0008_auto_20170117_0453'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='custom_invoice_id',
            field=models.CharField(blank=True, default=None, max_length=255, null=True),
        ),
        migrations.RunSQL(["""
            UPDATE lorikeet_order
            SET custom_invoice_id=NULL
            WHERE custom_invoice_id=''
        """]),
        migrations.AlterField(
            model_name='order',
            name='custom_invoice_id',
            field=models.CharField(blank=True, default=None, max_length=255, null=True, unique=True),
        ),
    ]