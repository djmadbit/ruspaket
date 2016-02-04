# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-01-31 14:29
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0007_auto_20160126_2113'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='min_order',
            field=models.CharField(default='', max_length=255, verbose_name='\u041c\u0438\u043d\u0438\u043c\u0430\u043b\u044c\u043d\u044b\u0439 \u0437\u0430\u043a\u0430\u0437'),
        ),
        migrations.AddField(
            model_name='item',
            name='min_order',
            field=models.CharField(default='', max_length=255, verbose_name='\u041c\u0438\u043d\u0438\u043c\u0430\u043b\u044c\u043d\u044b\u0439 \u0437\u0430\u043a\u0430\u0437'),
        ),
        migrations.AlterField(
            model_name='category',
            name='min_count',
            field=models.CharField(default='', max_length=255, verbose_name='\u041c\u0438\u043d\u0438\u043c\u0430\u043b\u044c\u043d\u043e\u0435 \u043a\u043e\u043b\u0438\u0447\u0435\u0441\u0442\u0432\u043e'),
        ),
        migrations.AlterField(
            model_name='item',
            name='min_count',
            field=models.CharField(default='', max_length=255, verbose_name='\u041c\u0438\u043d\u0438\u043c\u0430\u043b\u044c\u043d\u043e\u0435 \u043a\u043e\u043b\u0438\u0447\u0435\u0441\u0442\u0432\u043e'),
        ),
    ]
