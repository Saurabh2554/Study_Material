from broker import RedisStreamBroker
import time

class StreamConsumer:
    def consume_redis_events(self):
        broker = RedisStreamBroker()
        last_id = '123'

        while True:
            events = broker.read_event(last_id)
            print(events)
            if events:
                for stream, data in events:
                    for msg_id, msg_data in data:
                        print(f"Received ID: {msg_id}, Data: {msg_data}")
                        last_id = msg_id  # Move pointer

            else:
                print("Waiting for new events...")
                time.sleep(10)
            time.sleep(2)    
                

if __name__ == "__main__":
    consumer = StreamConsumer()
    consumer.consume_redis_events()