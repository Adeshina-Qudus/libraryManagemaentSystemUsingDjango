from django.urls import path
from . import views

urlpatterns = [
    path('books/', views.BookList.as_view(), name='books'),
    path('books/<int:pk>', views.book_details, name='book_details'),
    path('author', views.author_list),
    # path('author/)
]
