from kafka import KafkaConsumer


consumer = KafkaConsumer(bootstrap_servers="localhost:9092")
consumer.subscribe(['informations_about_device'])  #the topic name of subscribed data is very, VERY important

for streamRecords in consumer:
    print(streamRecords[6])



"""kafka producer could read some data generated by wmi module method and then - he could pass them to the kafka
consumer for further analysis"""