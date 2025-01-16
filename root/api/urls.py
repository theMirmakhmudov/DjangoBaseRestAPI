from rest_framework.routers import DefaultRouter
from .views import BookViewSet, CategoryViewSet

router = DefaultRouter()
router.register(r'books', BookViewSet, basename='books')
router.register(r'category', CategoryViewSet, basename="category")

urlpatterns = router.urls
