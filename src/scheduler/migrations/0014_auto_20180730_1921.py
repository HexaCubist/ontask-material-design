# -*- coding: utf-8 -*-
# Generated by Django 1.11.14 on 2018-07-30 09:51
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('scheduler', '0013_auto_20180730_1918'),
    ]

    operations = [
        migrations.AlterField(
            model_name='scheduledemailaction',
            name='bcc_email',
            field=models.CharField(blank=True, default='', max_length=2048, verbose_name='Comma-separated list of BCC Emails'),
        ),
        migrations.AlterField(
            model_name='scheduledemailaction',
            name='cc_email',
            field=models.CharField(blank=True, default='', max_length=2048, verbose_name='Comma-separated list of CC Emails'),
        ),
    ]
