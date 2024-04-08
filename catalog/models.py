from uuid import uuid4

from django.db import models
from django.conf import settings


# Create your models here.

class Book(models.Model):
    Book_CHOICES = [
        ('P', 'Politics'),
        ('F', "Finance"),
        ('R', "Romance")
    ]
    title = models.CharField(max_length=255)
    summary = models.TextField()
    isbn = models.CharField(max_length=10)
    genre = models.CharField(max_length=1, choices=Book_CHOICES, default='F')
    author = models.ForeignKey('Author', on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.title} {self.isbn} {self.summary}"


class Author(models.Model):
    name = models.CharField(max_length=50)
    date_of_birth = models.DateField(null=True, blank=True)
    date_of_death = models.DateField(blank=True, null=True)

    def __str__(self):
        return f"{self.name}"


class Language(models.Model):
    name = models.CharField(max_length=255)


class BookInstance(models.Model):
    AVAILABLE = 'A'
    UNAVAILABLE = 'U'
    STATUS_CHOICES = [
        (AVAILABLE, 'Available'),
        (UNAVAILABLE, 'Unavilable')
    ]
    unique_id = models.UUIDField(default=uuid4, primary_key=True)
    due_back = models.DateField()
    status = models.CharField(max_length=1, choices=STATUS_CHOICES, default=AVAILABLE)
    book = models.ForeignKey(Book, on_delete=models.PROTECT)
    borrower = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.PROTECT)

    def __str__(self):
        return f"{self.unique_id} {self.due_back} {self.status} {self.borrower}"
