from rest_framework import serializers


class BookSerializer(serializers.Serializer):
    title = serializers.CharField(max_length=225)
    summary = serializers.CharField(max_length=1000)
    isbn = serializers.CharField(max_length=20)
