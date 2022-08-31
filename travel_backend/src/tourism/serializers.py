from rest_framework import serializers
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
from src.core.choices import ROOM_CHOICES, TOURS_CHOICES


class CountriesSerializer(serializers.ModelSerializer):
    travels = serializers.StringRelatedField()
    excursions = serializers.StringRelatedField()

    class Meta:
        model = Countries
        fields = (
            'name',
            'language',
            'description',
            'visa',
            'insurance',
            'mem',
            'transfer',
            'support',
            'travels',
            'excursions',
        )


class TravelSerializer(serializers.ModelSerializer):
    travel_hotel = serializers.StringRelatedField()
    travel_tour = serializers.StringRelatedField()

    class Meta:
        model = Travel
        fields = (
            'name',
            'description',
            'rating',
            'travel_hotel',
            'travel_tour',
        )


class HotelSerializer(serializers.HyperlinkedModelSerializer):
    room_types = serializers.ChoiceField(choices=ROOM_CHOICES)
    hotel_photo = serializers.ImageField(max_length=None, allow_empty_file=False, use_url=True)

    class Meta:
        model = Hotel
        fields = (
            'name',
            'description',
            'stars',
            'rating',
            'price',
            'room_types',
            'hotel_photo',
        )


class HotelPhotoSerializer(serializers.ModelSerializer):

    class Meta:
        model = HotelPhoto
        fields = '__all__'


class TourSerializer(serializers.ModelSerializer):
    tour_type = serializers.ChoiceField(choices=TOURS_CHOICES)
    places = serializers.StringRelatedField()
    agency = serializers.StringRelatedField()

    class Meta:
        model = Tour
        fields = (
            'name',
            'description',
            'tour_type',
            'rating',
            'places',
            'agency',
        )


class ExcursionSerializer(serializers.ModelSerializer):
    owner = serializers.StringRelatedField()

    class Meta:
        model = Excursion
        fields = (
            'name',
            'description',
            'rating',
            'price',
            'owner',
        )


class InterestingPlaceSerializer(serializers.HyperlinkedModelSerializer):
    excursions = serializers.StringRelatedField()
    place_photo = serializers.ImageField(max_length=None, allow_empty_file=False, use_url=True)

    class Meta:
        model = InterestingPlace
        fields = (
            'name',
            'description',
            'history',
            'rating',
            'excursions',
            'place_photo',
        )


class PlacePhotoSerializer(serializers.ModelSerializer):

    class Meta:
        model = PlacePhoto
        fields = '__all__'


class AgencySerializer(serializers.ModelSerializer):

    class Meta:
        model = Agency
        fields = '__all__'
