from django.test import TestCase
from restaurant.models import Menu, Booking
from restaurant.serializers import MenuSerializer
from rest_framework.test import APIClient
from rest_framework.test import status

class AnimalTestCase(TestCase):
    def setUp(self):
        self.client = APIClient()
        Menu.objects.create(title="Pizza", price=15, inventory=100)
        Menu.objects.create(title="Burger", price=8, inventory=200)
    
    def test_getall(self):
        response = self.client.get('/menu/')
        menus = Menu.objects.all()
        serializer = MenuSerializer(menus, many=True)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, serializer.data)