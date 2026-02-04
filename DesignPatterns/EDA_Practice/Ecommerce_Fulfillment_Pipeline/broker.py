import redis

class RedisStreamBroker:
    def __init__(self, stream="order_event"):
        self.stream = stream
        self.r = redis.Redis(host="localhost",port=6379,db=0)

    def publishGroupEvent(self,event,stream=None):
        try:
            print(type(event))
            self.r.xadd(stream or self.stream,event)
        except Exception as e:
            print(f"error publishing event... {e}")    

    def readGroupEvent(self,groupName, consumerName):
        try:
            """
            . The Role of >: Unique Assignment (WHO)
            When you pass {stream: ">"}:
            Action: You are telling Redis: "Only give me messages that have NOT YET been delivered to any consumer in my group."
            Result: Redis checks its internal group pointer and assigns the next available block of messages (starting from the stream's logical end) to your consumer. This is the load-balancing step. The messages are moved to your consumer's Pending Entries List (PEL) even before they are returned.
            Crucial Point: Once a message is assigned to you, it is immediately invisible to all other consumers in the group.

            
            If you set count=10,The Reality of the Batch
            Step 1: Assignment,Redis identifies the next 10 unread messages in the stream log.
            Step 2: Delivery,Redis assigns all 10 messages to your consumer's PEL.
            Step 3: Return,Redis returns those same 10 messages to your application code.
            """
            message = self.r.xreadgroup(
                groupName, 
                consumerName, 
                {self.stream: '>'}, 
                count=5, 
                block=1000
            )
            return message
        except Exception as ex:
            print(f"error while reading event.. {ex}") 

    def createGroup(self,groupName,id='0',mkStream=False):
        try:
            self.r.xgroup_create(self.stream,groupName,id='0',mkstream=mkStream) 
            print(f"Group: {groupName} created for the stream {self.stream}.")
        except Exception as e:
            print(f"error creating group...: {e}")

    def acknowledge(self,GROUP_NAME,acknowledged_ids):
        self.r.xack(self.stream, GROUP_NAME, *acknowledged_ids)          