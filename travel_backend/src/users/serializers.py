from rest_framework import serializers
from src.users.models import Customer, Favorite


class CustomerSerializer(serializers.ModelSerializer):
    cars_list = serializers.StringRelatedField()

    class Meta:
        model = Customer
        fields = (
            'id',
            'first_name',
            'last_name',
            'username',
            'date_joined',
            'is_staff',
            'is_active',
            'is_excursion_owner',
            'email',
            'balance',
            'avatar',
            'cars_list',
        )


class FavoriteSerializer(serializers.ModelSerializer):
    owner = serializers.StringRelatedField()
    favorite_tour = serializers.StringRelatedField()

    class Meta:
        model = Favorite
        fields = ('owner', 'favorite_tour',)
