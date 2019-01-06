# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('contenttypes', '0002_remove_content_type_name'),
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='AnotherModel',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
            ],
        ),
        migrations.CreateModel(
            name='MyModel',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('object_id', models.PositiveIntegerField()),
                ('content_type', models.ForeignKey(to='contenttypes.ContentType')),
            ],
        ),
        migrations.AlterModelOptions(
            name='post',
            options={'verbose_name': 'blog post', 'ordering': ['-pub_date', 'title'], 'permissions': (('view_future_post', 'Can view unpublished Post'),), 'get_latest_by': 'pub_date'},
        ),
    ]
