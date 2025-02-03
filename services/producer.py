from kafka import KafkaProducer
import json
import random
import time
import numpy as np

print('test')

KAFKA_TOPIC = "ais.raw.data"
KAFKA_BROKER = "kafka:9092"

producer = KafkaProducer(
    bootstrap_servers=KAFKA_BROKER,
    value_serializer=lambda v: json.dumps(v).encode('utf-8')
)

def generate_ais_message():
    return {
        "mmsi": random.randint(431661000, 431661999),
        "lat": round(34.5605 + np.random.uniform(-0.01, 0.01), 6),
        "lon": round(134.1590 + np.random.uniform(-0.01, 0.01), 6),
        "speed": round(random.uniform(0, 15), 1),
        "course": random.randint(0, 360),
        "heading": random.randint(0, 360),
        "timestamp": int(time.time())
    }

while True:
    message = generate_ais_message()
    producer.send(KAFKA_TOPIC, message)
    print(f"Produced: {message}")
    time.sleep(1)
