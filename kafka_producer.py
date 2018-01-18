from kafka import KafkaProducer
import wmisample

try:
    producer = KafkaProducer(bootstrap_servers="localhost:9092")
    particular_data = wmisample.GetSomeParticularData()
    while True:
        for i in particular_data:
            producer.send(topic='informations_about_device', value=bytes(str(i).encode()))

except Exception as e:
    print(e)



"""how to send array of string values as a bytes variables?
got an pretty nice idea :D"""