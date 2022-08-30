from django.contrib.auth.models import AbstractUser
from django.db import models


class Customer(AbstractUser):
    avatar = models.ImageField(upload_to='avatars/', verbose_name='Customer avatar')
    balance = models.DecimalField(
        default=None,
        null=True,
        blank=True,
        max_digits=14,
        decimal_places=2,
        verbose_name='Customer balance'
    )
    is_excursion_owner = models.BooleanField(default=False, verbose_name='Excursion owner')

    def __str__(self):
        return f'{self.first_name, self.last_name, self.balance}'

    class Meta:
        db_table = 'customer'
        verbose_name = 'Customer'
        verbose_name_plural = 'Customers'
        ordering = ('id',)


class Favorite(models.Model):
    owner = models.ForeignKey(
        to='users.Customer',
        on_delete=models.SET_NULL,
        null=True,
        verbose_name='Favorites owner',
        related_name='favorites_owner'
    )
    favorite_tour = models.ForeignKey(
        to='tourism.Tour',
        on_delete=models.SET_NULL,
        null=True,
        verbose_name='Favorite tour',
        related_name='favorite_tour'
    )

    def __str__(self):
        return f'{self.owner, self.favorite_tour}'

    class Meta:
        db_table = 'favorite'
        verbose_name = 'Favorite'
        verbose_name_plural = 'Favorites'
        ordering = ('id',)
