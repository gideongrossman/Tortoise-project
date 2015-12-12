# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('turtle_shell', '0004_animal_animal_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='animal',
            name='animal_email',
        ),
    ]
