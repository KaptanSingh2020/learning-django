# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20190105_2003'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='post',
            options={'verbose_name': 'blog post', 'ordering': ['-pub_date', 'title'], 'permissions': (('view_future_post', 'Can view unpublished Post'), ('view_post', 'Can view Post')), 'get_latest_by': 'pub_date'},
        ),
    ]
