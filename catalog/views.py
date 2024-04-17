from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.


def book_list(request):
    return HttpResponse('books')


def book_details(request, id):
    return HttpResponse(id)

