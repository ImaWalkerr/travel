import pytest
from rest_framework.test import APIClient
from django.urls import reverse


@pytest.mark.django_db
def test_country_view():
    api_client = APIClient()
    url = reverse('tourism: countries')
    response = api_client.get(url)

    assert response.status_code == 200


@pytest.mark.django_db
def test_travel_view():
    api_client = APIClient()
    url = reverse('tourism: travels')
    response = api_client.get(url)

    assert response.status_code == 200


@pytest.mark.django_db
def test_hotel_view():
    api_client = APIClient()
    url = reverse('tourism: hotels')
    response = api_client.get(url)

    assert response.status_code == 200


@pytest.mark.django_db
def test_excursion_view():
    api_client = APIClient()
    url = reverse('tourism: excursions')
    response = api_client.get(url)

    assert response.status_code == 200
