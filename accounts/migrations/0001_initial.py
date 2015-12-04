# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='softlayer_api',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', primary_key=True, serialize=False)),
                ('username', models.CharField(max_length=64)),
                ('api_key', models.CharField(max_length=255)),
                ('endpoint_url', models.CharField(max_length=1024)),
            ],
        ),
    ]
