from django.contrib import admin
from src.tourism.models import (
    Travel,
    Hotel,
    HotelPhoto,
    Tour,
    Excursion,
    InterestingPlace,
    PlacePhoto,
    Agency,
)


@admin.register(Travel)
class TravelAdmin(admin.ModelAdmin):
    pass


@admin.register(Hotel)
class HotelAdmin(admin.ModelAdmin):
    pass


@admin.register(HotelPhoto)
class HotelPhotoAdmin(admin.ModelAdmin):
    pass


@admin.register(Tour)
class TourAdmin(admin.ModelAdmin):
    pass


@admin.register(Excursion)
class ExcursionAdmin(admin.ModelAdmin):
    pass


@admin.register(InterestingPlace)
class InterestingPlaceAdmin(admin.ModelAdmin):
    pass


@admin.register(PlacePhoto)
class PlacePhotoAdmin(admin.ModelAdmin):
    pass


@admin.register(Agency)
class AgencyAdmin(admin.ModelAdmin):
    pass
