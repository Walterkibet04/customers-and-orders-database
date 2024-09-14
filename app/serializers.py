from rest_framework import serializers
from .models import Order
from .models import Customer

class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields =  '__all__' # ['name', 'phoneNumber', 'code']

class OrderSerializer(serializers.ModelSerializer):
    # customer = CustomerSerializer(read_only=True)
    class Meta:
        model = Order
        fields = '__all__' # ['item', 'amount', 'time', 'customer'] 