from django.urls import path
from .views import ProductViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()

router.register(r'products', ProductViewSet, basename='product') 

# The router returns a list of URL patterns
urlpatterns = router.urls