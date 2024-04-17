from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response


# Create your views here.

@api_view()
def book_list(request):

    return Response('books')


@api_view()
def book_details(request, id):
    return Response(id)
