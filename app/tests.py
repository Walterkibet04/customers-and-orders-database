from django.test import TestCase
from rest_framework.test import APITestCase
from django.urls import reverse
from rest_framework import status
from .models import Customer, Order
from unittest.mock import patch
from rest_framework.test import APIClient
from .views import OrderViewSet
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

class TestCustomerAPI(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.customer_data={
            "name": "kibet",
            "phoneNumber": "+254708783067",
            "code": "123456"

        }
    
    def test_create_customer(self):
        response = self.client.post(reverse('customer-list'), self.customer_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Customer.objects.count(), 1)
        self.assertEqual(Customer.objects.get().name, "kibet")

class TestOrderAPI(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.customer = Customer.objects.create(
            name= "kibet",
            phoneNumber= "+254708783067",
            code= "123456"
        )
        self.order_data = {
            "customer": self.customer.id,
            "item": "milk",
            "amount": 65
        }
    # @patch('orders.views.OrderViewSet.send_sms')  # mock sending sms
    # def test_create_order(self, mock_send_sms):
    #     mock_send_sms.return_value = 'fake_message_sid' 
    #     response = self.client.post(reverse('order-list'), self.order_data, format='json')
    #     self.assertEqual(response.status_code, status.HTTP_201_CREATED)
    #     self.assertEqual(Order.objects.count(), 1)
    #     self.assertEqual(Order.objects.get().item, "milk")
    #     mock_send_sms.assert_called_once() 

        