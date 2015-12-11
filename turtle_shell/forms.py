from django import forms
from django.forms import ModelForm
from .models import Animal

class NameForm(forms.Form):
    your_name = forms.CharField(label='Your name', max_length=100)

class ContactForm(forms.Form):
    subject = forms.CharField(max_length=100)
    message = forms.CharField(widget=forms.Textarea)
    sender = forms.EmailField()
    cc_myself = forms.BooleanField(required=False)
    
#class AnimalForm(forms.Form):
#    animal_species = forms.CharField(max_length=100)
#    image = forms.ImageField()
#    email = forms.EmailField()

class AnimalForm(ModelForm):
    class Meta:
        model = Animal
        fields = ['animal_species', 'animal_image', 'animal_email']