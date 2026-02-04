import redis

class RedisStreamBroker:
    def __init__(self, stream = "event_stream"):
        self.stream = stream
        self.r = redis.Redis(host='localhost', port=6379, db=0)

    def add_event(self,event):
        try:
            self.r.xadd(self.stream, event) 
        except Exception as e:
            print("error adding event to stream... ",e)

        
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