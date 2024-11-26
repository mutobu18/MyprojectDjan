from django.db import models

# Create your models here.

class Customer(models.Model):
    
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=15, blank=True, null=True)
    address = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name
    
class Order(models.Model):
    order_date = models.DateTimeField(auto_now_add=True)
    total_amount = models.DecimalField(max_digits=10, decimal_places=2)
    customer = models.ForeignKey(Customer, related_name='orders', on_delete=models.CASCADE)

    def __str__(self):
        return f"Order {self.id} by {self.customer.name}"