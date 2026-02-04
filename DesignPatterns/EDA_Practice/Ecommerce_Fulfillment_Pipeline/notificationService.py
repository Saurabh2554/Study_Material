from groupManager import GroupManager
from broker import RedisStreamBroker
from helpers import parse_message

class NotificationService:
    def __init__(self,groupName="notification_group"):
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
                #Send email to each customer regarding their order
                print("Email sent..")
                self.ackEvent(ack_ids)

        except Exception as ex:
            print(f"error consuming event... {ex}")
        


if __name__ == "__main__":
    import sys
    notification = NotificationService()
    if len(sys.argv) > 1:
        notification.consumeEvent(sys.argv[1])
    else:
        print("Usage: python consumer_script.py <consumer_name>")