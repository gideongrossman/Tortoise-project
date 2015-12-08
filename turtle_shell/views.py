from django.http import HttpResponse


def index(request):
    return HttpResponse("Hello, world. You're at the turtle_shell index.")
    
def person(request):
    return HttpResponse("You're on the person page now.")