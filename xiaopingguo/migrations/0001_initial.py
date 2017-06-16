# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User_info',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('type', models.CharField(default='\u62bd\u5956', max_length=15, verbose_name=b'\xe7\x94\xa8\xe6\x88\xb7\xe7\xb1\xbb\xe5\x9e\x8b')),
                ('name', models.CharField(max_length=31, verbose_name=b'\xe7\x94\xa8\xe6\x88\xb7\xe5\xa7\x93\xe5\x90\x8d')),
                ('phone', models.CharField(max_length=11, verbose_name=b'\xe7\x94\xa8\xe6\x88\xb7\xe6\x89\x8b\xe6\x9c\xba\xe5\x8f\xb7\xe7\xa0\x81')),
                ('address', models.CharField(max_length=250, verbose_name=b'\xe7\x94\xa8\xe6\x88\xb7\xe5\x9c\xb0\xe5\x9d\x80')),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name='\u7528\u6237\u521b\u5efa\u65f6\u95f4')),
                ('add_more', models.CharField(max_length=500, null=True, verbose_name='\u5907\u6ce8', blank=True)),
                ('surplus_apple', models.CharField(max_length=10, null=True, verbose_name='\u5269\u4f59\u82f9\u679c\u6570', blank=True)),
            ],
            options={
                'ordering': ['create_time'],
                'verbose_name': '\u7528\u6237\u4fe1\u606f',
                'verbose_name_plural': '\u7528\u6237\u4fe1\u606f',
            },
        ),
    ]
