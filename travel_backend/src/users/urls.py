from django.urls import path, include
from src.users.views import CustomerViewSet, FavoriteViewSet
from rest_framework import routers


router = routers.DefaultRouter()
router.register(r'customer', CustomerViewSet, basename='customer')
router.register(r'customer_favorites', FavoriteViewSet, basename='customer_favorites')

urlpatterns = [
    path('customer/', include(router.urls)),
]
