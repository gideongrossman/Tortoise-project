# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('turtle_shell', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Person',
            new_name='Animal',
        ),
        migrations.RenameField(
            model_name='animal',
            old_name='person_name',
            new_name='animal_species',
        ),
    ]
