from groupManager import GroupManager
from broker import RedisStreamBroker
from helpers import parse_message

class ShipmentService:
    def __init__(self,groupName="shipment_group"):
        self.broker = RedisStreamBroker()
        self.group = groupName
    
    def ackEvent(self,acknowledgeIds):
        try:
            self.broker.acknowledge(self.group,acknowledgeIds)
        except Exception as e:
            print(f"Error while acknowledgement in group {self.group}")

    def consumeEvent(self,consumerName):
        try:
            GroupManager(self.group).createConsumerGroup()
            message_list = self.broker.readGroupEvent(self.group,consumerName)
           
            if message_list and len(message_list)>0:
                ack_ids, decoded_data = parse_message(message_list)
                #Shipment logic
                print("shipment done..")

                self.ackEvent(ack_ids)

        except Exception as ex:
            print(f"error consuming event... {ex}")
        


if __name__ == "__main__":
    import sys
    shipment = ShipmentService()
    if len(sys.argv) > 1:
        shipment.consumeEvent(sys.argv[1])
    else:
        print("Usage: python consumer_script.py <consumer_name>")