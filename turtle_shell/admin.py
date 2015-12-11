from django.contrib import admin
from models import Animal
# Register your models here.

class AnimalAdmin(admin.ModelAdmin):
    fieldsets = [
    (None, {'fields': ['animal_species']}),
    ('The document', {'fields':['animal_image']}),
    (None, {'fields':['animal_email']}),
    ]
    search_fields=['animal_species']
    
admin.site.register(Animal, AnimalAdmin)