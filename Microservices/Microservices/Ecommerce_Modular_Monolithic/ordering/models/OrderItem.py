from django.db import models
from .order import Order
from product.models import Product

class OrderItem(models.Model):
    order = models.ForeignKey(
            Order,
            on_delete=models.CASCADE, 
            related_name='items'
    )

    product = models.ForeignKey(
        Product,
        on_delete=models.PROTECT,
    )

    quantity = models.IntegerField()
    unit_price = models.DecimalField(max_digits=10, decimal_places=2)

    def total_price(self):
        return self.quantity * self.unit_price
    
    def __str__(self):
        return f"{self.quantity} x {self.product.name} in Order #{self.order.id}"
    
