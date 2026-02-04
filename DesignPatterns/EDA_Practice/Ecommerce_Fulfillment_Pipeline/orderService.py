#order service will act as a producer.
"""
Right now our order service(Producer) is having a bug named (Dual write problem). Suppose our order service first update the order table marked as order created and then publishes the event to redis using xadd. Then possible scenarios may happen:
  1. What if after creating order record the event publishing step fails due to say networlk timeout or redis was down. Resulting i will have an order but the further process say shipping never happend, leading to order deadlock.

  To overcome this issue and make producer robust(avoid Dual write problem) we use a concept named (Outbox Pattern).

  Further read about Outbox pattern, Dual-write problem and CDC.

"""

from broker import RedisStreamBroker
from event import ORDER_PLACED_EVENT
from groupManager import GroupManager
from helpers import parse_message
import copy
import time
import json

MESSAGE_OUTBOX = {
    "inventory": {"SKU-A": 100, "SKU-B": 50},
    "outbox": [], # Stores events to be relayed
    "idempotency": set() # Stores processed message IDs
}

class OrderService:
    def __init__(self,groupName = "order_group"):
        self.broker = RedisStreamBroker()
        self.group = groupName

    def produceOrderEvent(self):
        try:
            event = copy.copy(ORDER_PLACED_EVENT)
            for i in range(1,5):
                print(f"Publishing order no: {i}")
                event['order_id'] = event['order_id'] + 1
                # save order to DB

                # In real world this will be a db transaction
                MESSAGE_OUTBOX["outbox"].append({
                    "topic":"order_event",
                    "paylod":event,
                })
                self.broker.publishGroupEvent(event)
                print("Next order will be placed after 5 sec..")
                time.sleep(8)
            
        except Exception as e:
            print(f"Error creating event. {e}")
    
    # the CDC implementation
    def run_outbox_retry(self):
        while True:
            new_event = MESSAGE_OUTBOX["outbox"].pop(0)
            if new_event:
                self.broker.publishGroupEvent(new_event["payload"],new_event["topic"])
            else:
                print("waiting for new data in CDC...")

            time.sleep(5)    

    #Producer can also act as consumer when InventoryService fires inventory_restored event
    # In that case we will have to delete the order history from db
    
    def ackEvent(self, ack_ids):pass

    def consumeReverseOrderEvent(self,consumerName):
        try:
            GroupManager(self.group).createConsumerGroup()
            message_list = self.broker.readGroupEvent(self.group,consumerName)

            if message_list and len(message_list)>0:
                # check_and_process_idempotent() call
                ack_ids, decoded_data = parse_message(message_list)

                # Revert the order created from Order DB
 
                self.ackEvent(ack_ids)

        except Exception as ex:
            print("error reventing order")            
              

if __name__ == "__main__":
    OrderService().produceOrderEvent()