"""
Here we have a major flaw regarding idempotency. My order can be processed twice if our service breaks between inventory update and acknowledgement. For that we need to implement idempotency check. We can implement it in two ways:
   1. use redis in-memory cache to store idempotency keys and further check before actual processing. But it can get reset if redis restarts or server restart. Also in first time, if after setting the idempotency key the db operations failed, in that case we again won't be able to process our valid order.

   2. Use a dedicated table in database for such kind of thing, and at the same time first update the actual inventory operation table update(EX: reduce product count), then insert the row in idempotency table regarding that operation. Commit db(DB-Transaction) operations only happen when both process successfully ends. in case of any failure just rollback the operation.

Also our consumer is implementing unidirectional communication i.e. reads event from OrderService. But there may be scenario when after managing/locking products after updated consumer itself should fire an event say "InventoryRestored" and further our payment service reads this event and process payment.  

Also payment service can back fire an event say "PaymentDeclined" then in that case we will have to remove/free the inventory which we locked for any particular pdt. Also we may need to delete the order saved in db when InventoryService fires an event say "InventoryRestored". 

So in short our producer/consumer should be ready to produce as well as consume events at the same time.
In order to deliver/solve such scenario, we would need to implement (SAGA Pattern).
"""
from groupManager import GroupManager

from broker import RedisStreamBroker
from helpers import parse_message, check_and_process_idempotent

class InventoryService:
    def __init__(self,groupName="inventory_group"):
        self.broker = RedisStreamBroker()
        self.group = groupName
    
    def ackEvent(self,acknowledgeIds):
        try:
            if acknowledgeIds and len(acknowledgeIds) > 0:
                self.broker.acknowledge(self.group,acknowledgeIds)

            print("Inventory updated..")
        except Exception as e:
            print(f"Error while acknowledgement in group {self.group}")

    def consumeEvent(self,consumerName):
        try:
            GroupManager(self.group).createConsumerGroup()
            message_list = self.broker.readGroupEvent(self.group,consumerName)
           
            if message_list and len(message_list)>0:
                # check_and_process_idempotent() call
                ack_ids, decoded_data = parse_message(message_list)

                self.ackEvent(ack_ids)

        except Exception as ex:
            print(f"error consuming event... {ex}")
        


if __name__ == "__main__":
    import sys
    inventory = InventoryService()
    if len(sys.argv) > 1:
        inventory.consumeEvent(sys.argv[1])
    else:
        print("Usage: python consumer_script.py <consumer_name>")