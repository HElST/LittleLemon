from django.test import TestCase
from restaurant.models import Menu
from django.test import Client

class AnimalTestCase(TestCase):
    def setUp(self):
        Menu.objects.create(title="Mint IceCream", price=80, inventory=100)
        Menu.objects.create(title="Lemon IceCream", price=10, inventory=200)
    
    def test_getall(self):
        menu_all = Menu.objects.all()