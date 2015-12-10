from __future__ import unicode_literals

from django.db import models

# Create your models here.


class Animal(models.Model):
    animal_species = models.CharField(max_length=200)
    document = models.FileField(upload_to='documents')
    def __str__(self):
        return self.animal_species