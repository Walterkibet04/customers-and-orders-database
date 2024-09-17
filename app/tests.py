from django.test import TestCase
from rest_framework.test import APITestCase
from django.urls import reverse
from rest_framework import status
from .models import Customer, Order

# Create your tests here.
# class TestCustomerModel(APITestCase):
#     def test_customer_create(self):
#         sample_customer = {"name":"kibet", "phoneNumber":"0708783067", "code":"37236139"}
#         response = self.client.post(reverse('customers'), sample_customer)
#         self.assertEqual(response.status_code, status.HTTP_201_CREATED)

class TestCustomerModel(TestCase):
    def setUp(self):
        self.customer = Customer.objects.create(name = "kibet", phoneNumber = "0708783067", code = "37236139")

    def test_customer_creation(self):
         self.assertEqual(self.customer.name, "kibet")
         self.assertEqual(self.customer.phoneNumber, "0708783067")
         self.assertEqual(self.customer.code, "37236139")

class TestOrderModel(TestCase):
    def setUp(self):
        self.customer = Customer.objects.create(name = "kibet", phoneNumber = "0708783067", code = "37236139")
        self.order = Order.objects.create(
            customer = self.customer,
            item = "milk",
            amount=65
        )
    def test_order_creation(self):
         self.assertEqual(self.order.item, "milk")
         self.assertEqual(self.order.amount, 65)
         self.assertEqual(self.order.customer.name, "kibet")