from django.db import models
from .enums import ProductAvailabilityStatus
import uuid
# Create your models here.

class Product(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=255, unique=True, null=False, blank=False)
    description = models.TextField(null=False, blank=False)
    price = models.DecimalField(max_digits=10, decimal_places=2, null=False, blank=False)
    imageUrl = models.URLField(max_length=2000, null=True, blank=True, default='')
    qty_avl = models.IntegerField(
        default=0,
        null=False,
        help_text="Number of units available for sale."
    )
    status = models.CharField(
        max_length=50,
        choices=ProductAvailabilityStatus.choices(),
        default=ProductAvailabilityStatus.OUT_OF_STOCK.value,
        null=False
    )


    def __str__(self):
        return self.name