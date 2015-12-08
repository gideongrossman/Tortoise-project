from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return HttpResponse("Hello, world. You're at the turtle_shell index.")
    
def person(request):
    return render(request, 'turtle_shell/people_index.html')