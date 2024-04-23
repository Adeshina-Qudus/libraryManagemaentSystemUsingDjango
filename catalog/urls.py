from rest_framework_nested import routers

from . import views

router = routers.DefaultRouter()
router.register("books", views.BookViewSet, "books")
router.register("author", views.AuthorViewSet, "author")
router.register("review", views.ReviewViewSet, "review")

review_router = routers.NestedDefaultRouter(router, "books", lookup='book')
review_router.register("reviews", views.ReviewViewSet, "review")

urlpatterns = router.urls + review_router.urls
