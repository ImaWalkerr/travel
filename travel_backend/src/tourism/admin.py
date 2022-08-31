from django.contrib import admin
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


@admin.register(Countries)
class TravelAdmin(admin.ModelAdmin):
    fieldsets = (
        ('Country info:', {
            'fields': (
                ('name', 'language'),
                'description',
            )
        }),
        ('Info for customer:', {
            'fields': (
                ('visa', 'insurance', 'mem', 'transfer'),
                'support',
                ('travels', 'excursions'),
            )
        }),
    )
    list_display = ('name', 'language', 'description',)
    list_filter = ('name', 'language',)
    search_fields = ('name',)
    list_display_links = ('name',)


@admin.register(Travel)
class TravelAdmin(admin.ModelAdmin):
    fieldsets = (
        ('Travel main info:', {
            'fields': (
                ('name', 'rating'),
                'description',
            )
        }),
        ('Travel contains:', {
            'fields': (
                ('travel_hotel', 'travel_tour',),
            )
        }),
    )
    list_display = ('name', 'description', 'rating',)
    list_filter = ('name', 'rating',)
    search_fields = ('name',)
    list_display_links = ('name',)


@admin.register(Hotel)
class HotelAdmin(admin.ModelAdmin):
    fieldsets = (
        ('Hotel main info:', {
            'fields': (
                ('name', 'rating', 'price'),
                'description',
            )
        }),
        ('Hotel extra:', {
            'fields': (
                'room_types',
                'hotel_photo',
            )
        }),
    )
    list_display = ('name', 'price', 'rating',)
    list_filter = ('name', 'rating',)
    search_fields = ('name',)
    list_display_links = ('name',)


@admin.register(HotelPhoto)
class HotelPhotoAdmin(admin.ModelAdmin):
    fieldsets = (
        ('Hotel photos:', {
            'fields': (
                'description',
                'photo',
            )
        }),
    )
    list_display = ('description',)
    list_display_links = ('description',)


@admin.register(Tour)
class TourAdmin(admin.ModelAdmin):
    fieldsets = (
        ('Tour main info:', {
            'fields': (
                ('name', 'rating'),
                'description',
            )
        }),
        ('Tour contains:', {
            'fields': (
                ('tour_type', 'agency'),
                'places',
            )
        }),
    )
    list_display = ('name', 'tour_type', 'rating',)
    list_filter = ('name', 'rating',)
    search_fields = ('name',)
    list_display_links = ('name',)


@admin.register(Excursion)
class ExcursionAdmin(admin.ModelAdmin):
    fieldsets = (
        ('Excursion main info:', {
            'fields': (
                ('name', 'rating', 'price'),
                'description',
                'owner',
            )
        }),
    )
    list_display = ('name', 'price', 'rating',)
    list_filter = ('name', 'rating',)
    search_fields = ('name',)
    list_display_links = ('name',)


@admin.register(InterestingPlace)
class InterestingPlaceAdmin(admin.ModelAdmin):
    fieldsets = (
        ('Place main info:', {
            'fields': (
                ('name', 'rating'),
                ('history', 'description'),
            )
        }),
        ('Place contains:', {
           'fields': (
               ('excursions', 'place_photo'),
           )
        }),
    )
    list_display = ('name', 'rating',)
    list_filter = ('name', 'rating',)
    search_fields = ('name',)
    list_display_links = ('name',)


@admin.register(PlacePhoto)
class PlacePhotoAdmin(admin.ModelAdmin):
    fieldsets = (
        ('Place photos:', {
            'fields': (
                'description',
                'photo',
            )
        }),
    )
    list_display = ('description',)
    list_display_links = ('description',)


@admin.register(Agency)
class AgencyAdmin(admin.ModelAdmin):
    fieldsets = (
        ('Agency main info:', {
            'fields': (
                ('name', 'rating'),
                'description',
            )
        }),
        ('Tour price:', {
           'fields': (
               ('price', 'discount'),
           )
        }),
    )
    list_display = ('name', 'description', 'rating',)
    list_filter = ('name', 'rating',)
    search_fields = ('name',)
    list_display_links = ('name',)
