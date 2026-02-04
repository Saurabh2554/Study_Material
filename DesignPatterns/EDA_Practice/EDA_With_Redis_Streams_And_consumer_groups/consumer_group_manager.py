from broker import RedisStreamBroker
class ConsumerGroupManager:
    def __init__(self, stream,group_name,start_id, mkStream=False):
        self.stream=stream
        self.group = group_name
        self.start = start_id
        self.mkstream = mkStream

    def setup_consumer_group(self):
        try:
            broker = RedisStreamBroker(self.stream)
            broker.r.xgroup_create(self.stream, self.group, self.start,mkstream=self.mkstream)    
            print(f"Group '{self.group}' created for stream '{self.stream}'.")     
        except Exception as e:
            print(f"error creating consumer group: {e}")    
