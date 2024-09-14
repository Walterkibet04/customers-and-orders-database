from django.db import models

# Create your models here.
class Customer(models.Model):
    name = models.CharField(max_length=200)
    phoneNumber =  models.CharField(max_length = 15)
    # email = models.EmailField()
    code = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Order(models.Model):
    item = models.CharField(max_length=200)
    amount = amount = models.DecimalField(max_digits=10, decimal_places=2)
    time = models.DateTimeField(auto_now_add=True)
    customer = models.ForeignKey(Customer, related_name='orders', on_delete = models.CASCADE)

    def __str__(self):
        return f"Item {self.item}  by {self.customer.name} code {self.customer.code}"