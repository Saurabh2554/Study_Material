from consumer_group_manager import ConsumerGroupManager
from config import STREAM_NAME, START_ID, GROUP_NAME
from broker import RedisStreamBroker
import time

def consumer_worker(consumer_name):
    """The main consumer logic."""
    ConsumerGroupManager(STREAM_NAME,GROUP_NAME,START_ID,True).setup_consumer_group()
    
    print(f"\n--- Consumer {consumer_name} Ready ---")
    broker = RedisStreamBroker(STREAM_NAME)

    while True:
        try:
            messages = broker.read_group_event(GROUP_NAME,consumer_name)
            
            if messages:
                stream_messages = messages[0][1] 
            
                acknowledged_ids = [] 
                for message_id, data in stream_messages:
                    print(message_id, data['text'])
                    time.sleep(0.1) 
                    
                    acknowledged_ids.append(message_id)

                if acknowledged_ids:
                    broker.acknowledge(GROUP_NAME,acknowledged_ids)
                    print(f"[{consumer_name}] Successfully ACKed {len(acknowledged_ids)} messages.")

            else:
                print(f"[{consumer_name}] No new messages. Blocking...")
                time.sleep(5)
        
        except KeyboardInterrupt:
            break

if __name__ == "__main__":
    # To run this, you must run two separate Python processes:
    # 1. python consumer_script.py worker-A
    # 2. python consumer_script.py worker-B
    import sys
    
    if len(sys.argv) > 1:
        consumer_worker(sys.argv[1])
    else:
        print("Usage: python consumer_script.py <consumer_name>")