# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('xiaopingguo', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user_info',
            name='score',
            field=models.CharField(max_length=10, null=True, verbose_name='\u5206\u6570', blank=True),
        ),
    ]
