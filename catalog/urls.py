from django.urls import path, include
from rest_framework.routers import SimpleRouter

from . import views

router = SimpleRouter()
router.register("books", views.BookViewSet, "books")
urlpatterns = [
    # path('books/', views.BookList.as_view(), name='books'),
    # path('books/<int:pk>', views.BookDetails.as_view(), name='book_details'),
    path('', include(router.urls)),
    path('author/', views.AuthorList.as_view()),
    path('author/<int:pk>', views.AuthorDetails.as_view())
    # path('author/)
]
