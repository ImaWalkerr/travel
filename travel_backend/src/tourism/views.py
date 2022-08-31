from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets, filters
from src.core.permissions import IsAdminOrReadOnly
from src.tourism.models import (
    Countries,
    Travel,
    Hotel,
    HotelPhoto,
    Tour,
    Excursion,
    InterestingPlace,
    PlacePhoto,
    Agency,
)
from src.tourism.serializers import (
    CountriesSerializer,
    TravelSerializer,
    HotelSerializer,
    HotelPhotoSerializer,
    TourSerializer,
    ExcursionSerializer,
    InterestingPlaceSerializer,
    PlacePhotoSerializer,
    AgencySerializer,
)


class CountriesViewSet(viewsets.ModelViewSet):
    queryset = Countries.objects.all()
    serializer_class = CountriesSerializer
    permission_classes = (IsAdminOrReadOnly,)
    filter_backends = (DjangoFilterBackend, filters.SearchFilter,)
    filterset_fields = ('name', 'language',)
    search_fields = ('name', 'language',)
    ordering_fields = ('name',)


class TravelViewSet(viewsets.ModelViewSet):
    queryset = Travel.objects.all()
    serializer_class = TravelSerializer
    permission_classes = (IsAdminOrReadOnly,)
    filter_backends = (DjangoFilterBackend, filters.SearchFilter,)
    filterset_fields = ('name', 'rating',)
    search_fields = ('name',)
    ordering_fields = ('name',)


class HotelViewSet(viewsets.ModelViewSet):
    queryset = Hotel.objects.all()
    serializer_class = HotelSerializer
    permission_classes = (IsAdminOrReadOnly,)
    filter_backends = (DjangoFilterBackend, filters.SearchFilter,)
    filterset_fields = ('name', 'stars', 'rating',)
    search_fields = ('name', 'stars',)
    ordering_fields = ('name',)


class HotelPhotoViewSet(viewsets.ModelViewSet):
    queryset = HotelPhoto.objects.all()
    serializer_class = HotelPhotoSerializer


class TourViewSet(viewsets.ModelViewSet):
    queryset = Tour.objects.all()
    serializer_class = TourSerializer
    permission_classes = (IsAdminOrReadOnly,)
    filter_backends = (DjangoFilterBackend, filters.SearchFilter,)
    filterset_fields = ('name', 'tour_type', 'rating',)
    search_fields = ('name', 'tour_type',)
    ordering_fields = ('name',)


class ExcursionViewSet(viewsets.ModelViewSet):
    queryset = Excursion.objects.all()
    serializer_class = ExcursionSerializer
    permission_classes = (IsAdminOrReadOnly,)
    filter_backends = (DjangoFilterBackend, filters.SearchFilter,)
    filterset_fields = ('name', 'rating', 'price',)
    search_fields = ('name', 'owner',)
    ordering_fields = ('name',)


class InterestingPlaceViewSet(viewsets.ModelViewSet):
    queryset = InterestingPlace.objects.all()
    serializer_class = InterestingPlaceSerializer
    permission_classes = (IsAdminOrReadOnly,)
    filter_backends = (DjangoFilterBackend, filters.SearchFilter,)
    filterset_fields = ('name', 'rating',)
    search_fields = ('name',)
    ordering_fields = ('name',)


class PlacePhotoViewSet(viewsets.ModelViewSet):
    queryset = PlacePhoto.objects.all()
    serializer_class = PlacePhotoSerializer


class AgencyViewSet(viewsets.ModelViewSet):
    queryset = Agency.objects.all()
    serializer_class = AgencySerializer
    permission_classes = (IsAdminOrReadOnly,)
    filter_backends = (DjangoFilterBackend, filters.SearchFilter,)
    filterset_fields = ('name', 'rating', 'price', 'discount',)
    search_fields = ('name',)
    ordering_fields = ('name',)
