# -*- coding: utf-8 -*-
# Generated by Django 1.11.14 on 2018-08-26 09:38
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('scheduler', '0026_auto_20180826_1853'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='scheduledaction',
            name='bcc_email',
        ),
        migrations.RemoveField(
            model_name='scheduledaction',
            name='cc_email',
        ),
        migrations.RemoveField(
            model_name='scheduledaction',
            name='send_confirmation',
        ),
        migrations.RemoveField(
            model_name='scheduledaction',
            name='subject',
        ),
        migrations.RemoveField(
            model_name='scheduledaction',
            name='track_read',
        ),
    ]
