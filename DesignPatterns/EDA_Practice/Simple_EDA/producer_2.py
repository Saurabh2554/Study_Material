from broker import SimpleBroker, RedisBroker
from event import simple_event
import time
class SimpleProducer:
    def produceEvents(cls):
        broker = SimpleBroker()
        count=0
        event = simple_event.copy()
        while count<5:
            print(f"producing event count: {count}")
            event["type"] = f"hello world event {count}"
            event["msg"] = f"hello! welcome to EDA tutorial {count}"
            broker.add_event(event)
            count= count+1
            print(count)
            time.sleep(3)

    def produceEventsTORedis(cls):
        broker = RedisBroker()
        count=0
        event = simple_event.copy()
        while count<5:
            print(f"producing event count: {count}")
            event["id"] = count
            event["message"] = f"hello! welcome to EDA tutorial from producer_2 {count}"
            broker.publish_event(event)
            count= count+1
            print(count)
            time.sleep(3)
        

    
    #this method is just used to depict as how does producer remain functionable even in case of consumer failure. Promoting decoupling
    def calculateSum(self):
        return 1+2    

if __name__ == "__main__":
    producer = SimpleProducer()
    producer.produceEventsTORedis()
        