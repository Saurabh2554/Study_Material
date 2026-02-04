from broker import SimpleBroker,RedisBroker
import time

class SimpleConsumer:
    def consume_events(cls):
        broker = SimpleBroker()

        while True:
            print("waiting for event to receive... ")
            event = broker.get_event()
            if event is not None:
                print(f"Received event: {event['msg']}")
                break
            
            time.sleep(1)

    def consume_redis_events(self):
        print("listening...")
        broker = RedisBroker()
        broker.listen()
                

if __name__ == "__main__":
    consumer = SimpleConsumer()
    consumer.consume_redis_events()