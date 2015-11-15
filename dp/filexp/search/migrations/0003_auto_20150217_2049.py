# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('search', '0002_auto_20150217_2042'),
    ]

    operations = [
        migrations.RenameField(
            model_name='page',
            old_name='tags',
            new_name='profile',
        ),
    ]
