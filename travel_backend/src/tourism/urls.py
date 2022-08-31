from django.urls import path, include
from src.tourism.views import (
    CountriesViewSet,
    TravelViewSet,
    HotelViewSet,
    HotelPhotoViewSet,
    TourViewSet,
    ExcursionViewSet,
    InterestingPlaceViewSet,
    PlacePhotoViewSet,
    AgencyViewSet,
)
from rest_framework import routers


router = routers.DefaultRouter()
router.register(r'countries', CountriesViewSet, basename='countries')
router.register(r'travels', TravelViewSet, basename='travels')
router.register(r'hotels', HotelViewSet, basename='hotels')
router.register(r'hotel_photos', HotelPhotoViewSet, basename='hotel_photos')
router.register(r'tours', TourViewSet, basename='tours')
router.register(r'hotels', HotelViewSet, basename='hotels')
router.register(r'excursions', ExcursionViewSet, basename='excursions')
router.register(r'places', InterestingPlaceViewSet, basename='places')
router.register(r'place_photos', PlacePhotoViewSet, basename='place_photos')
router.register(r'agencies', AgencyViewSet, basename='agencies')

urlpatterns = [
    path('tourism/', include(router.urls)),
]