from django.contrib import admin
from src.users.models import Customer, Favorite


@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    fieldsets = (
        ('Customer info:', {
            'fields': (
                ('first_name', 'last_name', 'username'),
                'avatar',
                ('email', 'password'),
                ('balance', 'is_excursion_owner'),
            )
        }),
        ('Extra info:', {
            'fields': (
                'date_joined',
                ('is_superuser', 'is_staff', 'is_active',),
            )
        }),
    )
    list_display = ('username', 'email', 'balance',)
    list_filter = ('username', 'balance',)
    search_fields = ('username',)
    list_display_links = ('username',)


@admin.register(Favorite)
class FavoriteAdmin(admin.ModelAdmin):
    fieldsets = (
        ('Favorite info:', {
            'fields': (
                'owner',
                'favorite_tour',
            )
        }),
    )
    list_display = ('owner', 'favorite_tour',)
    list_filter = ('owner',)
    list_display_links = ('owner',)
