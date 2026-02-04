import queue
import redis
import json

class SimpleBroker:
    def __init__(self):
        self.event_queue = queue.Queue()

    def add_event(self,event:dict):
        self.event_queue.put(event)  

    def get_event(self):
        return self.event_queue.get()

class RedisBroker:
    def __init__(self,channel="events"):
        self.channel = channel
        self.r = redis.Redis(host='localhost', port=6379, db=0)
        

    def publish_event(self,event:dict):
        try:
            print("self.r.ping()")
            self.r.publish(self.channel, json.dumps(event))
        except Exception as e:
            print(e)
       

    def listen(self):
        pubsub = self.r.pubsub()
        print(pubsub)
        pubsub.subscribe(self.channel)

        print(f"Subscribed to channel: {self.channel}")
        for msg in pubsub.listen():
            print(msg)
            if msg["type"] == "message":
                print(msg["data"])
                data = json.loads(msg["data"])
                print("received dict:", data)
                print("id:", data["id"])
                print("message:", data["message"])      