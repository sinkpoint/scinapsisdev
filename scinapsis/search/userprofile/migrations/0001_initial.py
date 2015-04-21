# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='AddressModel',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('street', models.CharField(default=b'', max_length=20)),
                ('province', models.CharField(default=b'', max_length=20)),
                ('country', models.CharField(default=b'', max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='PhoneModel',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('phone_number', models.CharField(blank=True, max_length=15, validators=[django.core.validators.RegexValidator(regex=b'^\\+?1?\\d{9,15}$', message=b"Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")])),
            ],
        ),
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('first_name', models.CharField(default=b'', max_length=20)),
                ('middle_name', models.CharField(default=b'', max_length=20)),
                ('last_name', models.CharField(default=b'', max_length=20)),
                ('email', models.EmailField(max_length=254)),
                ('image_link', models.CharField(default=b'', max_length=20)),
                ('address', models.ForeignKey(to='userprofile.AddressModel')),
                ('phone', models.ForeignKey(to='userprofile.PhoneModel')),
                ('user', models.OneToOneField(to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
