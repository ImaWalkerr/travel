from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from src.core.choices import ROOM_CHOICES, STANDARD


class Travel(models.Model):
    name = models.CharField(max_length=255, verbose_name='Travel name')
    description = models.TextField(max_length=10000, blank=True, verbose_name='Travel description')
    rating = models.IntegerField(
        default=5,
        validators=[
            MinValueValidator(0),
            MaxValueValidator(10)
        ],
        verbose_name='Travel rating'
    )
    travel_hotel = models.ForeignKey(
        to='tourism.Hotel',
        on_delete=models.SET_NULL,
        null=True,
        verbose_name='Travel hotel',
        related_name='travel_hotel'
    )
    travel_tour = models.ForeignKey(
        to='tourism.Tour',
        on_delete=models.SET_NULL,
        null=True,
        verbose_name='Travel tour',
        related_name='travel_tour'
    )

    def __str__(self):
        return f'{self.name, self.description, self.rating}'

    class Meta:
        db_table = 'travel'
        verbose_name = 'Travel'
        verbose_name_plural = 'Travels'
        ordering = ('id',)


class Hotel(models.Model):
    name = models.CharField(max_length=255, verbose_name='Hotel name')
    description = models.TextField(max_length=10000, blank=True, verbose_name='Hotel description')
    stars = models.PositiveIntegerField(
        default=3,
        validators=[
            MinValueValidator(0),
            MaxValueValidator(5)
        ],
        verbose_name='Hotel stars'
    )
    rating = models.IntegerField(
        default=5,
        validators=[
            MinValueValidator(0),
            MaxValueValidator(10)
        ],
        verbose_name='Hotel rating'
    )
    price = models.DecimalField(
        default=None,
        null=True,
        blank=True,
        max_digits=14,
        decimal_places=2,
        verbose_name='Hotel price for week'
    )
    room_types = models.CharField(
        choices=ROOM_CHOICES,
        default=STANDARD,
        max_length=255,
        verbose_name='Hotel room choices'
    )
    hotel_photo = models.ManyToManyField(
        to='tourism.HotelPhoto',
        verbose_name='Hotel photo',
        related_name='hotel_photo'
    )

    def __str__(self):
        return f'{self.name, self.description, self.rating}'

    class Meta:
        db_table = 'hotel'
        verbose_name = 'Hotel'
        verbose_name_plural = 'Hotels'
        ordering = ('id',)


class HotelPhoto(models.Model):
    description = models.CharField(max_length=255, verbose_name='Hotel photo description')
    photo = models.ImageField(upload_to='hotels/', verbose_name='Hotel photo')

    def __str__(self):
        return f'{self.description}'

    class Meta:
        db_table = 'hotel_photo'
        verbose_name = 'HotelPhoto'
        verbose_name_plural = 'HotelPhotos'
        ordering = ('id',)


class Tour(models.Model):
    name = models.CharField(max_length=255, verbose_name='Tour name')
    description = models.TextField(max_length=10000, blank=True, verbose_name='Tour description')
    rating = models.IntegerField(
        default=5,
        validators=[
            MinValueValidator(0),
            MaxValueValidator(10)
        ],
        verbose_name='Agency rating'
    )
    places = models.ManyToManyField(
        to='tourism.InterestingPlace',
        verbose_name='List of interesting places',
        related_name='list_of_places'
    )
    agency = models.ForeignKey(
        to='tourism.Agency',
        on_delete=models.SET_NULL,
        null=True,
        verbose_name='Tour agency',
        related_name='tour_agency'
    )

    def __str__(self):
        return f'{self.name, self.description, self.rating}'

    class Meta:
        db_table = 'tour'
        verbose_name = 'Tour'
        verbose_name_plural = 'Tours'
        ordering = ('id',)


class Excursion(models.Model):
    name = models.CharField(max_length=255, verbose_name='Place name')
    description = models.TextField(max_length=10000, blank=True, verbose_name='Place description')
    rating = models.IntegerField(
        default=5,
        validators=[
            MinValueValidator(0),
            MaxValueValidator(10)
        ],
        verbose_name='Agency rating'
    )
    price = models.DecimalField(
        default=None,
        null=True,
        blank=True,
        max_digits=14,
        decimal_places=2,
        verbose_name='Excursion price from customer'
    )
    owner = models.ForeignKey(
        to='users.Customer',
        on_delete=models.SET_NULL,
        null=True,
        verbose_name='Excursion owner',
        related_name='excursion_owner'
    )

    def __str__(self):
        return f'{self.name, self.description, self.rating}'

    class Meta:
        db_table = 'excursion'
        verbose_name = 'Excursion'
        verbose_name_plural = 'Excursions'
        ordering = ('id',)


class InterestingPlace(models.Model):
    name = models.CharField(max_length=255, verbose_name='Place name')
    description = models.TextField(max_length=10000, blank=True, verbose_name='Place description')
    history = models.TextField(max_length=10000, blank=True, verbose_name='Place history')
    rating = models.IntegerField(
        default=5,
        validators=[
            MinValueValidator(0),
            MaxValueValidator(10)
        ],
        verbose_name='Agency rating'
    )
    excursions = models.ManyToManyField(
        to='tourism.Excursion',
        verbose_name='Place excursions',
        related_name='place_excursions'
    )
    place_photo = models.ManyToManyField(
        to='tourism.PlacePhoto',
        verbose_name='Place photo',
        related_name='place_photo'
    )

    def __str__(self):
        return f'{self.name, self.description, self.rating}'

    class Meta:
        db_table = 'interesting_place'
        verbose_name = 'InterestingPlace'
        verbose_name_plural = 'InterestingPlaces'
        ordering = ('id',)


class PlacePhoto(models.Model):
    description = models.CharField(max_length=255, verbose_name='Place photo description')
    photo = models.ImageField(upload_to='places/', verbose_name='Places photo')

    def __str__(self):
        return f'{self.description}'

    class Meta:
        db_table = 'place_photo'
        verbose_name = 'PlacePhoto'
        verbose_name_plural = 'PlacePhotos'
        ordering = ('id',)


class Agency(models.Model):
    name = models.CharField(max_length=255, verbose_name='Agency name')
    description = models.TextField(max_length=10000, blank=True, verbose_name='Agency description')
    rating = models.IntegerField(
        default=5,
        validators=[
            MinValueValidator(0),
            MaxValueValidator(10)
        ],
        verbose_name='Agency rating'
    )
    price = models.DecimalField(
        default=None,
        null=True,
        blank=True,
        max_digits=14,
        decimal_places=2,
        verbose_name='Tour price from agency'
    )
    discount = models.DecimalField(
        default=None,
        null=True,
        blank=True,
        max_digits=14,
        decimal_places=2,
        verbose_name='Tour discount from agency'
    )

    def __str__(self):
        return f'{self.name, self.description, self.rating}'

    class Meta:
        db_table = 'agency'
        verbose_name = 'Agency'
        verbose_name_plural = 'Agencies'
        ordering = ('id',)
