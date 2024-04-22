from rest_framework import serializers
from .models import *


class BookSerializer(serializers.ModelSerializer):
    # author = serializers.HyperlinkedRelatedField(
    #     queryset=Author.objects.all(),
    #     view_name='author_details'
    # )

    # title = serializers.CharField(max_length=225)
    # summary = serializers.CharField(max_length=1000)
    # isbn = serializers.CharField(max_length=20)
    class Meta:
        model = Book
        fields = ['title', 'summary', 'isbn', 'author']


class AuthorSerializer(serializers.ModelSerializer):
    # first_name = serializers.CharField(max_length=50)
    # last_name = serializers.CharField(max_length=50)

    class Meta:
        model = Author
        fields = ['first_name', 'last_name']
