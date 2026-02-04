from producer import SimpleProducer

if __name__ == "__main__":
    producer = SimpleProducer()
    producer.produceEventsTORedis()
    

