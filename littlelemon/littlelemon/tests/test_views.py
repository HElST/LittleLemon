from django.test import TestCase
from restaurant.models import MenuItem, Booking
from restaurant.serializers import MenuSerializer
from django.test import Client
from rest_framework import status


class AnimalTestCase(TestCase):
    def setUp(self):
        MenuItem.objects.create(title="Pizza", price=15, inventory=100)
        MenuItem.objects.create(title="Burger", price=8, inventory=200)
    
    def test_getall(self):
        c = Client()
        response = c.get('/restaurant/menu/')
        menus = MenuItem.objects.all()
        serializer = MenuSerializer(menus, many=True)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, serializer.data)