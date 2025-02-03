from kafka import KafkaConsumer, KafkaProducer
import json

KAFKA_RAW_TOPIC = "ais.raw.data"
KAFKA_VALID_TOPIC = "ais.valid.data"
KAFKA_BAD_TOPIC = "ais.bad.data"
KAFKA_BROKER = "kafka:9092"

consumer = KafkaConsumer(
    KAFKA_RAW_TOPIC,
    bootstrap_servers=KAFKA_BROKER,
    auto_offset_reset="earliest",
    value_deserializer=lambda v: json.loads(v.decode('utf-8'))
)

producer = KafkaProducer(
    bootstrap_servers=KAFKA_BROKER,
    value_serializer=lambda v: json.dumps(v).encode('utf-8')
)

def validate_ais_data(data):
    return 30 <= data["lat"] <= 40 and 130 <= data["lon"] <= 140 and 0 <= data["speed"] <= 50

for message in consumer:
    data = message.value
    if validate_ais_data(data):
        producer.send(KAFKA_VALID_TOPIC, data)
        print(f"Valid AIS Data: {data}")
    else:
        producer.send(KAFKA_BAD_TOPIC, data)
        print(f"Invalid AIS Data: {data}")
