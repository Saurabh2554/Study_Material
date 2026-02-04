import redis
import time
from event import simple_event
from broker import RedisStreamBroker
from config import STREAM_NAME

class ConsumerGroupProducer:
    def ProduceEvents():
        try:
            broker = RedisStreamBroker(stream=STREAM_NAME)
            event = simple_event.copy()
            for i in range(1,5):
                print(f"producing event with id: {i}")
                event['id'] = i
                event['message'] = f"Message no: {i}"
                broker.publish_event(event)
                time.sleep(6)

        except Exception as e:
            print(f"error publishing event: {e}")

if __name__ == "__main__":
    ConsumerGroupProducer.ProduceEvents()