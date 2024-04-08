from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.

def greet(request):
    return render(request, '../demo/templates/hello.html')


def greet_me(request, name):
    return HttpResponse(f"let's xplore django...{name}")
