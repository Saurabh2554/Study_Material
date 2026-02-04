from ..models import Product
from decimal import Decimal
from .product_queries import get_product_by_name
from ..enums import ProductAvailabilityStatus
from django.db import transaction, models
from django.core.exceptions import ObjectDoesNotExist
import uuid

def create_new_product(name:str, description:str, price:Decimal, image_url:str):

    if price<Decimal('0.01'):
        raise ValueError("Product price must be greater than zero.")
    
    if Product.objects.filter(name__iexact=name).exists():
        raise ValueError(f"Product with the name '{name}' already exists.")
    
    product = Product.objects.create(
        id = uuid.uuid4(),
        name = name,
        description = description,
        price = price,
        imageUrl = image_url
    )

    return product

@transaction.atomic
def update_product_inventory(pdt_id:str, qty_ordered:int):

    try:
        product = Product.objects.select_for_update().get(id=pdt_id) # select_for_update() locks the row until the end of the transaction
    except ObjectDoesNotExist:
        raise ValueError(f"Product with ID {pdt_id} not found.") 
    
    if product.qty_avl < qty_ordered:
        raise ValueError("Insufficient stock available for this order.")
    
    product.qty_avl -= qty_ordered

    if product.qty_avl == 0:
        new_status = ProductAvailabilityStatus.OUT_OF_STOCK.value
    else:
        new_status = ProductAvailabilityStatus.IN_STOCK.value    
    
    product.status = new_status
    product.save()
    



