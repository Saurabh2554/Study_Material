from broker import RedisStreamBroker
from event import simple_event
import time

class StreamProducer:
    def produceEventsTORedis(cls):
        broker = RedisStreamBroker()
        count=0
        event = simple_event.copy()
        while count<5:
            print(f"producing event count: {count}")
            event["id"] = f"tre_11cc_{count}"
            event["message"] = f"hello! with streams again: {count}"
            broker.add_event(event)
            count= count+1
            print(count)
            time.sleep(5)

if __name__ == "__main__":
    producer = StreamProducer()
    producer.produceEventsTORedis()
                    