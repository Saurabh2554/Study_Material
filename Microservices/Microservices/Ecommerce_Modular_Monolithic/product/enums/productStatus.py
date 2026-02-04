from enum import Enum

class ProductAvailabilityStatus(Enum):
    IN_STOCK = 'IN_STOCK'
    LOW_STOCK = 'LOW_STOCK'
    OUT_OF_STOCK = 'OUT_OF_STOCK'
    DISCONTINUED = 'DISCONTINUED'

    @classmethod
    def choices(cls):
        return [(key.value, key.name.replace('_', ' ').title()) for key in cls]