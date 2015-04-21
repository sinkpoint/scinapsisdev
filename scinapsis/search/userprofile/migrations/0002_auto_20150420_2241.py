# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('userprofile', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='address',
            field=models.ForeignKey(to='userprofile.AddressModel', null=True),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='phone',
            field=models.ForeignKey(to='userprofile.PhoneModel', null=True),
        ),
    ]
