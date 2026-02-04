import time

ORDER_PLACED_EVENT = {
    # --- Business Data (for Inventory/Shipping) ---
    
    # 1. Unique identifier for the transaction (Crucial for Idempotency)
    "order_id": 1001,
    
    # List of items being ordered
    # "items": [
    #     {"sku": "SKU-A101", "quantity": 2, "price": 49.99},
    #     {"sku": "SKU-B202", "quantity": 1, "price": 129.50},
    # ],
    
    # "shipping_address": {
    #     "street": "123 Event Stream Way",
    #     "city": "Decoupled City",
    #     "zip": "10101"
    # },
    "timestamp": int(time.time()),
    "retry_attempts": 0,
    # "last_error": None
}