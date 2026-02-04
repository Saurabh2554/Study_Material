from config import STREAM_NAME, GROUP_NAME, RETRY_CONSUMER_NAME, IDLE_TIME_MS
from broker import RedisStreamBroker

class RetryEvent:
    def process_retry(claimed_message):
        broker = RedisStreamBroker(STREAM_NAME)
        if claimed_message and len(claimed_message)>0:
            print(f"Retrying claimed messages... {claimed_message} , {type (claimed_message)}" )
            broker.acknowledge(GROUP_NAME,claimed_message[0][0])
        else:
            print("All event claimed...")   


    def retry_worker():
        try:
            broker = RedisStreamBroker(STREAM_NAME)
            while True:
                pending_list = broker.get_pending_range(GROUP_NAME)
                if pending_list and len(pending_list)>0:
                    stale_ids = [msg['message_id'] for msg in pending_list]

                    claimed_message = broker.claim_pending_list(GROUP_NAME,stale_ids,RETRY_CONSUMER_NAME)
                    RetryEvent.process_retry(claimed_message)
                    
                else:
                    print(f"No pending message...")

        except Exception as e:
            print(f"Error_retrying... {e}")
        
if __name__ == "__main__":
    RetryEvent.retry_worker()        