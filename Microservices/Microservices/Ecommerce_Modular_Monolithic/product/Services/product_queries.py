from ..models import Product
import uuid

def get_product_by_id(product_id: uuid.UUID):
    return Product.objects.get(id = product_id)

def get_all_products():
    return Product.objects.all()

def get_product_by_name(name:str):
    return Product.objects.get(name=name)


    