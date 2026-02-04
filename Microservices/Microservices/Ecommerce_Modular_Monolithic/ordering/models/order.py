from django.db import models
from ordering.enums import OrderStatus
import uuid
# Create your models here.

class Order(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    created_at = models.DateTimeField(auto_now_add=True)
    status = models.CharField(
        max_length=50,
        choices=OrderStatus.choices(), 
        default=OrderStatus.PENDING.value,
        verbose_name="Order Status"
    )
    
    def __str__(self):
        return self.id + self.status

