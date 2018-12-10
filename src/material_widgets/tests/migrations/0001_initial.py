# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-11-15 06:28
from __future__ import absolute_import
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name=u'MaterialWidgetsForeignKeyTestModel',
            fields=[
                (u'id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name=u'ID')),
                (u'item', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name=u'MaterialWidgetsManyToManyTestModel',
            fields=[
                (u'id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name=u'ID')),
                (u'item', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name=u'MaterialWidgetsTestModel',
            fields=[
                (u'id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name=u'ID')),
                (u'big_integer_field', models.BigIntegerField(blank=True, null=True)),
                (u'boolean_field', models.BooleanField()),
                (u'char_field', models.CharField(blank=True, max_length=32, null=True)),
                (u'date_field', models.DateField(blank=True, null=True)),
                (u'date_time_field', models.DateTimeField(blank=True, null=True)),
                (u'decimal_field', models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True)),
                (u'email_field', models.EmailField(blank=True, max_length=254, null=True)),
                (u'file_field', models.FileField(blank=True, upload_to=u'')),
                (u'file_path_field', models.FilePathField(blank=True, path=u'/demo/images')),
                (u'float_field', models.FloatField(blank=True, null=True)),
                (u'integer_field', models.IntegerField(blank=True, null=True)),
                (u'generic_ip_address_field', models.GenericIPAddressField(blank=True, null=True)),
                (u'null_boolean_field', models.NullBooleanField()),
                (u'positive_integer_field', models.PositiveIntegerField(blank=True, null=True)),
                (u'positive_small_integer_field', models.PositiveSmallIntegerField(blank=True, null=True)),
                (u'slug_field', models.SlugField(blank=True, null=True)),
                (u'small_integer_field', models.SmallIntegerField(blank=True, null=True)),
                (u'text_field', models.TextField(blank=True, null=True)),
                (u'time_field', models.TimeField(blank=True, null=True)),
                (u'url_field', models.URLField(blank=True, null=True)),
                (u'foreign_key', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=u'material_widgets_tests.MaterialWidgetsForeignKeyTestModel')),
                (u'many_to_many_field', models.ManyToManyField(blank=True, to=u'material_widgets_tests.MaterialWidgetsManyToManyTestModel')),
            ],
        ),
    ]
