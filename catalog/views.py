import segno
from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import *
from .serializers import *


# Create your views here.

class BookList(APIView):
    def post(self, request):
        serializer = BookSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def get(self, request):
        book = Book.objects.all()
        serializer = BookSerializer(book, many=True, context={'request': request})
        return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(['GET', 'POST'])
def book_list(request):
    if request.method == "GET":
        book = Book.objects.all()
        serializer = BookSerializer(book, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    elif request.method == "POST":
        serializer = BookSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)


@api_view(['GET', 'POST', 'DELETE'])
def book_details(request, pk):
    book = get_object_or_404(Book, id=pk)
    if request.method == 'GET':
        serializer = BookSerializer(book)
        book_qrcode = segno.make_qr(book.title)
        book_qrcode.save("welcome.png")
        return Response(serializer.data, status=status.HTTP_200_OK)
    elif request.method == 'PUT':
        serializer = BookSerializer(book, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(status=status.HTTP_200_OK)
    elif request.method == 'DELETE':
        book.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


# @api_view(['PUT', 'DELETE', 'GET'])
# def author_details(request, pk):
#     author = get_object_or_404(Author, id=pk)
#     if request.method == 'GET':
#         serializer = AuthorSerializer(data=request.data)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         return Response(serializer.data, status=status.HTTP_200_OK)
#     elif request.method == 'DELETE':
#         author.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(['GET', 'POST'])
def author_list(request):
    if request.method == 'GET':
        author = Author.objects.all()
        serializer = AuthorSerializer(author, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    elif request.method == 'POST':
        serializer = AuthorSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
