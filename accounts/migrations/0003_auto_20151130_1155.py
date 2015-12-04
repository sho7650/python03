# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_customuser'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='softlayer_id',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
