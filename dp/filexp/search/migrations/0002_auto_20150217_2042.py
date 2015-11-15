# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0001_initial'),
        ('search', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='page',
            name='profile',
        ),
        migrations.AddField(
            model_name='page',
            name='tags',
            field=models.ManyToManyField(to='login.UserProfile'),
            preserve_default=True,
        ),
    ]
