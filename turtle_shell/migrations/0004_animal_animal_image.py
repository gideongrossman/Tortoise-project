# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('turtle_shell', '0003_auto_20151209_1653'),
    ]

    operations = [
        migrations.AddField(
            model_name='animal',
            name='animal_image',
            field=models.ImageField(null=True, upload_to='documents'),
        ),
    ]
