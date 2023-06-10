from kafka import KafkaConsumer
import time
import json
from sqlalchemy import create_engine
from sqlalchemy import text

engine = create_engine("postgresql+psycopg2://postgres:postgres@localhost:5432/KafkaConsumer")

consumer = KafkaConsumer(
  'signup-topic',
  bootstrap_servers=['accurate-joey-13614-us1-kafka.upstash.io:9092'],
  sasl_mechanism='SCRAM-SHA-256',
  security_protocol='SASL_SSL',
  sasl_plain_username='YWNjdXJhdGUtam9leS0xMzYxNCRJygqqOBl_7VeJycXpY23odeWTlW1MFtCkeP8',
  sasl_plain_password='7d3572585c064f7b82f8f92fa59c8f53',
  group_id='$GROUP_NAME',
  auto_offset_reset='earliest',
  value_deserializer=lambda x: json.loads(x.decode('utf-8'))

)

time.sleep(2)

for msg in consumer:
    print(msg)
    timestamp = msg.timestamp
    value = msg.value
    with engine.connect() as conn:
        conn.execute(text(
            f"INSERT INTO signup VALUES('{value['username']}','{value['password']}','{value['firstname']}','{value['lastname']}','{value['email']}',{timestamp});commit;"
        ))
        print("Data inserted successfully!")