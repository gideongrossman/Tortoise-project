# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('turtle_shell', '0002_auto_20151209_1358'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='animal',
            name='document',
        ),
        migrations.AddField(
            model_name='animal',
            name='animal_email',
            field=models.EmailField(max_length=254, null=True),
        ),
    ]
