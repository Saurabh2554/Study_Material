from enum import Enum

class OrderStatus(Enum):
    PENDING = 'PENDING'             # Initial state, waiting for confirmation/payment
    PROCESSING = 'PROCESSING'       # Payment confirmed, items being prepared
    SHIPPED = 'SHIPPED'             # Items have left the warehouse
    IN_TRANSIT = 'IN_TRANSIT'       # Shipped and currently moving toward the customer

    DELIVERED = 'DELIVERED'         # Delivered to the customer (Final Success)
    COMPLETED = 'COMPLETED'         # Synonymous with DELIVERED or final internal closing
    CANCELLED = 'CANCELLED'         # Canceled by user or admin (Final Failure)
    REFUNDED = 'REFUNDED'           # Payment was processed, but later reversed
    FAILED = 'FAILED'
    
    @classmethod
    def choices(cls):
        return [(key.value, key.name.replace('_', ' ').title()) for key in cls]