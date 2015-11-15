# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('first', '0007_auto_20141005_0826'),
    ]

    operations = [
        migrations.AlterField(
            model_name='restaurant',
            name='restaurant_rating',
            field=models.IntegerField(default=0, choices=[(1, b'Poor'), (2, b'Unsatisfactory'), (3, b'Average'), (4, b'Good'), (5, b'Excellent')]),
        ),
        migrations.AlterField(
            model_name='review',
            name='user',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL),
        ),
    ]
