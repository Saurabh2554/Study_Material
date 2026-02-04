import json
from typing import List, Tuple, Any, Dict
def parse_message(message_list: List) -> Tuple[List[str], List[Dict[str, Any]]]:
        """
        Parses the nested list structure returned by XREADGROUP.

        It extracts the acknowledgment IDs and the decoded event data.

        Args:
            message_list: The raw list of messages returned by r.xreadgroup.
                          Format: [ [b'stream_name', [(b'id', {b'key': b'value'}), ...]] ]

        Returns:
            A tuple containing:
            1. ack_ids (List[str]): List of message IDs for XACK.
            2. events (List[Dict]): List of decoded event dictionaries.
        """
        ack_ids: List[str] = []
        decoded_events: List[Dict[str, Any]] = []

        # 1. Outer loop: Iterate over streams (usually only one)
        for stream_name_bytes, messages_list in message_list:
            
            # 2. Inner loop: Iterate over the list of (ID, Data) tuples
            for message_id_bytes, data_bytes in messages_list:
                
                # A. Decode and capture the Message ID (Crucial for XACK)
                message_id = message_id_bytes.decode('utf-8')
                ack_ids.append(message_id)
                
                # B. Decode the event data keys and values
                event_data: Dict[str, Any] = {}
                for key_bytes, value_bytes in data_bytes.items():
                    key = key_bytes.decode('utf-8')
                    
                    # Ensure value is decoded. Handle potential None or non-byte values if necessary.
                    try:
                        value = value_bytes.decode('utf-8')
                    except AttributeError:
                        value = value_bytes
                    
                    # C. Check for JSON-serialized fields (e.g., 'items' or 'shipping_address')
                    # This logic assumes simple fields are left as strings, 
                    # and complex fields would need to be checked and deserialized.
                    if key in ['items', 'shipping_address']:
                        try:
                            # If we know it was serialized as JSON, deserialize it
                            event_data[key] = json.loads(value)
                        except json.JSONDecodeError:
                            event_data[key] = value # Fallback if not valid JSON
                    else:
                        event_data[key] = value

                # Append the fully decoded event data
                decoded_events.append(event_data)
                
        return ack_ids, decoded_events

# Assuming this check is inside your Inventory Service Worker class

def check_and_process_idempotent(self, message_id: str, event_data: dict, ttl_seconds=86400):
    """
    Performs an Idempotency Check using Redis SETNX before processing the event.

    Args:
        message_id: The unique stream ID (e.g., '1764652068380-0').
        event_data: The decoded event data.
        ttl_seconds: How long to keep the key (e.g., 24 hours).
    """
    # 1. Construct the unique idempotency key
    # Use the group name, stream name, and message ID for global uniqueness
    idempotency_key = f"idempotency:{self.stream}:{self.group}:{message_id}"
    
    try:
        # 2. Perform the atomic check using SET with NX (Not Exists) and EX (Expire)
        # SET returns True if the key was set (i.e., it was a new, unprocessed message)
        # SET returns False if the key already existed (i.e., it was a duplicate message)
        
        # We use the current consumer name as the value for auditing purposes
        return self.r.set(
            idempotency_key, 
            self.consumer, 
            nx=True, 
            ex=ttl_seconds
        )
    except Exception as e:
        print(f"Critical error during idempotency check: {e}")
        # Depending on criticality, you might log and exit or retry
        raise