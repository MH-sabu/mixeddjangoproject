# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('first', '0005_review_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='review',
            name='time',
            field=models.DateTimeField(default=datetime.date(2014, 10, 4), auto_now_add=True),
            preserve_default=False,
        ),
    ]
