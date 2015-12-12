from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from .forms import NameForm, ContactForm, AnimalForm
from django.core.urlresolvers import reverse
from django.core.mail import send_mail
from .models import Animal


def index(request):
    return HttpResponse("Hello, world. You're at the turtle_shell index.")
    
def animal(request):
    return render(request, 'turtle_shell/people_index.html')

def list(request):
    return render(request, 'turtle_shell/list.html', {'animals':Animal.objects.all()})
    
def get_name(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = AnimalForm(request.POST, request.FILES)
        # check whether it's valid:
        if form.is_valid():
            newAnimal = Animal(animal_species = request.POST['animal_species'], animal_image = request.FILES['animal_image'])
            newAnimal.save()
            return HttpResponseRedirect(reverse('turtle_shell:list_animals'))

    # if a GET (or any other method) we'll create a blank form
    else:
        form = AnimalForm()

    return render(request, 'turtle_shell/name.html', {'form': form})
    
def thanks(request):
    return HttpResponse("Thank you. Your form has been submitted.")