from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import viewsets, status
from rest_framework.decorators import api_view
from .models import Order, Customer
from rest_framework.views import APIView
from .serializers import CustomerSerializer, OrderSerializer


# Create your views here.

class CustomerViewSet(viewsets.ModelViewSet):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer


class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer

    def create(self, request, *args, **kwargs):
        
        response = super().create(request, *args, **kwargs)
        if response.status_code == status.HTTP_201_CREATED:
            order = Order.objects.get(id=response.data['id'])
        return response


    def send_sms(self, order):
        recipients = {customer.phoneNumber}
        message = f"Hi {customer.name}, your order for {order.item} has been placed successfully"

        sender = "19997"


        response = sms.send(message, [order.customer.phoneNumber])
        return response
        # try:
        #     response = self.sms.send(message, recipients)
        #     print(response)
        # except Exception as e:
        #     print (f'Walter, we have a problem: {e}')
















# @api_view(['GET', 'POST'])
# def orders(request):
#     return Response('list of orders today', status=status.HTTP_200_OK)


# class OrderList(APIView):
#     def get(self, request):
#         client = request.GET.get('client')
#         if (client):
#             return Response({"message":"list of orders by " + client}, status.HTTP_200_OK)

#         return Response({"message":"list of orders"}, status.HTTP_200_OK)

#     def post(self, request):
#         return Response({"title":request.data.get("title")}, status.HTTP_201_CREATED)

# class Order(APIView):
#     def get(self, request, pk):
#         return Response({"title":"single order with id " + str(pk)}, status.HTTP_200_OK)
