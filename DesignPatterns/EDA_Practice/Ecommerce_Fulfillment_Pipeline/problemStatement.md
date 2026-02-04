## 🎯 Harder Implementation Scenario: The E-Commerce Fulfillment Pipeline

### **The Goal**

Design and implement the core microservices components for an e-commerce order fulfillment pipeline using **Redis Streams** as the Event Broker.

### **The Architecture**

* **1 Stream:** `order_events`
* **1 Producer:** **Order Service** (FastAPI/Flask endpoint)
* **3 Consumers (Microservices):** Each must be a member of its own Consumer Group.

### **The Services & Events**

| Service Role | Consumer Group | Task | Events Produced |
| :--- | :--- | :--- | :--- |
| **Order Service** (Producer) | N/A | Receives API call, validates, and publishes the first event. | `OrderPlaced` |
| **Inventory Service** (Consumer 1) | `inventory_group` | Attempts to reserve stock. **This service is unstable.** | `StockReserved` or `StockFailed` |
| **Shipping Service** (Consumer 2) | `shipping_group` | Prepares the shipment label. **Must be idempotent.** | `ShipmentPrepared` |
| **Notification Service** (Consumer 3) | `notification_group` | Sends a confirmation email to the customer. | N/A |

### **The Key Challenges (The Hard Part)**

1.  **Load Balancing & Unique Processing:** Ensure the `OrderPlaced` event is processed by **exactly one** instance of the Inventory Service, Shipping Service, and Notification Service. (I.e., you need three separate `XREADGROUP` calls, one for each group).
2.  **The Unstable Service & Retries:**
    * The **Inventory Service** must simulate failure (e.g., raise an error 40% of the time).
    * You must implement a separate **Retry Worker** that uses **`XPENDING`** and **`XCLAIM`** to retry failed `OrderPlaced` events after a 1-minute idle time, up to a maximum of 3 times.
3.  **Idempotency Test:** The **Shipping Service** must be truly **idempotent**. If the Inventory Service successfully reserves stock but fails to acknowledge (`XACK`) and is retried, the Shipping Service will receive the `StockReserved` event twice. The Shipping Service **must not create two shipment labels.**
4.  **DLQ Implementation:** If the Inventory Service fails its 3rd retry attempt, the event must be written to a dedicated **DLQ Stream** (`order_events:dlq`).

### **Implementation Steps**

1.  **Producer (Order Service):** Write the FastAPI/Flask code to take an order and `XADD` the initial `OrderPlaced` event.
2.  **Consumer Services:** Implement three Python scripts (Inventory, Shipping, Notification), each running with its own unique `GROUP_NAME` and using the `XREADGROUP` command.
3.  **Retry Worker:** Implement the dedicated script that periodically runs the **`XPENDING`** and **`XCLAIM`** logic.
4.  **Idempotency Logic:** In the **Shipping Service**'s processing logic, use a Redis **Set** or **Hash** to store a record of processed messages (keyed by `event_id` or `order_id`) and check it before proceeding.

This scenario tests not only your Consumer Group knowledge but also forces you to think about error handling, service boundaries, and data integrity in a distributed environment. Good luck! 🚀