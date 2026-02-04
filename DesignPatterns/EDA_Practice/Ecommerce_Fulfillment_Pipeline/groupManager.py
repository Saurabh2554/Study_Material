from broker import RedisStreamBroker

class GroupManager:
    def __init__(self,groupName,stream="order_event"):
        self.stream = stream
        self.group = groupName
        self.broker = RedisStreamBroker(stream)

    def createConsumerGroup(self):
        self.broker.createGroup(self.group)    



