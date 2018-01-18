from kafka import KafkaProducer
import wmisample

try:
    producer = KafkaProducer(bootstrap_servers="localhost:9092")
    particular_data = wmisample.GetSomeParticularData()
    while True:
        producer.send(topic='informations_about_device', value=bytearray(particular_data))

except Exception as e:
    print(e)



"""how to send array of string values as a bytes variables?"""