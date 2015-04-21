# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('userprofile', '0002_auto_20150420_2241'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userprofile',
            name='image_link',
        ),
        migrations.AddField(
            model_name='userprofile',
            name='image',
            field=models.ImageField(null=True, upload_to=b'', blank=True),
        ),
        migrations.AlterField(
            model_name='addressmodel',
            name='street',
            field=models.CharField(default=b'', max_length=100),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='first_name',
            field=models.CharField(default=b'', max_length=50),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='last_name',
            field=models.CharField(default=b'', max_length=50),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='middle_name',
            field=models.CharField(default=b'', max_length=50),
        ),
    ]
