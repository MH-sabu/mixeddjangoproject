# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('search', '0003_auto_20150217_2049'),
    ]

    operations = [
        migrations.AddField(
            model_name='page',
            name='datetime',
            field=models.DateTimeField(default=datetime.datetime(2015, 2, 19, 18, 28, 36, 643361), verbose_name='date_publish'),
            preserve_default=False,
        ),
    ]
