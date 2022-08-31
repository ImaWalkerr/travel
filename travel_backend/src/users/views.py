from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets, filters
from src.core.permissions import IsAdminOrReadOnly
from src.users.models import Customer, Favorite
from src.users.serializers import CustomerSerializer, FavoriteSerializer


class CustomerViewSet(viewsets.ModelViewSet):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer
    permission_classes = (IsAdminOrReadOnly,)
    filter_backends = (DjangoFilterBackend, filters.SearchFilter,)
    filterset_fields = ('first_name', 'first_name', 'username', 'balance',)
    search_fields = ('first_name', 'first_name', 'username',)
    ordering_fields = ('username',)


class FavoriteViewSet(viewsets.ModelViewSet):
    queryset = Favorite.objects.all()
    serializer_class = FavoriteSerializer
    permission_classes = (IsAdminOrReadOnly,)
    filter_backends = (DjangoFilterBackend, filters.SearchFilter,)
    filterset_fields = ('owner', 'favorite_tour',)
    search_fields = ('owner', 'favorite_tour',)
    ordering_fields = ('owner',)
