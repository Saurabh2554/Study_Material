import redis

class RedisStreamBroker:
    def __init__(self, stream):
        self.stream = stream
        self.r = redis.Redis(host="localhost",port=6379,db=0)

    def publish_event(self,event):
        try:
            self.r.xadd(self.stream,event)
        except Exception as e:
            print(f"Error adding exception: {e}")   

    def read_event(self,last_id='123'):
        try:
            print(f"Reading event: {last_id}")
            events = ""
            # print(f"Deleting id: {last_id}")
            # self.r.xdel(self.stream, last_id)
            print(f"event returns: {self.r.xread({self.stream: last_id},block=0)}")
            return events
        except Exception as e:
            print("error reading stream: ",e) 
            return []  

    def read_group_event(self,GROUP_NAME,consumer_name):
        try:
            message = self.r.xreadgroup(
                GROUP_NAME, 
                consumer_name, 
                {self.stream: '>'}, # '>' means "read new messages assigned to me"
                count=5, 
                block=1000
            )
            return message
        except Exception as e:
            print(f"reading_group_exception: {e}")  

    def acknowledge(self,GROUP_NAME,acknowledged_ids):
        self.r.xack(self.stream, GROUP_NAME, *acknowledged_ids)  

    def get_pending_range(self,GROUP_NAME,oldest_message_count=10):
        return self.r.xpending_range(
            self.stream,
            GROUP_NAME, 
            '-', 
            '+', 
            oldest_message_count, 
        )
    
    def claim_pending_list(self, GROUP_NAME,stale_ids,RETRY_CONSUMER_NAME,IDLE_TIME_MS=6000):
        try:
            return self.r.xclaim(
                self.stream, 
                GROUP_NAME, 
                RETRY_CONSUMER_NAME, 
                IDLE_TIME_MS, # Minimum time message must be idle
                stale_ids
            )
        except Exception as e:
            print(f"error retrying pending events: {e}")                    

