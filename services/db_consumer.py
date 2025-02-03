import psycopg2
from kafka import KafkaConsumer
import json
import os

KAFKA_VALID_TOPIC = "ais.valid.data"
KAFKA_BROKER = "kafka:9092"

DB_HOST = os.getenv("DB_HOST", "postgres")
DB_USER = os.getenv("DB_USER", "postgres")
DB_PASS = os.getenv("DB_PASS", "password")
DB_NAME = os.getenv("DB_NAME", "ais_db")

conn = psycopg2.connect(f"dbname={DB_NAME} user={DB_USER} password={DB_PASS} host={DB_HOST}")
cursor = conn.cursor()

consumer = KafkaConsumer(
    KAFKA_VALID_TOPIC,
    bootstrap_servers=KAFKA_BROKER,
    auto_offset_reset="earliest",
    value_deserializer=lambda v: json.loads(v.decode('utf-8'))
)

for message in consumer:
    data = message.value
    cursor.execute("""
        INSERT INTO ais_positions (mmsi, lat, lon, speed, course, heading, geom)
        VALUES (%s, %s, %s, %s, %s, %s, ST_SetSRID(ST_MakePoint(%s, %s), 4326))
    """, (data["mmsi"], data["lat"], data["lon"], data["speed"], data["course"], data["heading"], data["lon"], data["lat"]))
    conn.commit()
    print(f"Stored AIS Data: {data}")
