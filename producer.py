from kafka import KafkaProducer
import time
import json
import random
 
producer = KafkaProducer(
  bootstrap_servers=['accurate-joey-13614-us1-kafka.upstash.io:9092'],
  value_serializer = lambda x: json.dumps(x).encode('utf-8'),
  sasl_mechanism='SCRAM-SHA-256',
  security_protocol='SASL_SSL',
  sasl_plain_username='YWNjdXJhdGUtam9leS0xMzYxNCRJygqqOBl_7VeJycXpY23odeWTlW1MFtCkeP8',
  sasl_plain_password='7d3572585c064f7b82f8f92fa59c8f53',
)                    

# publish random message to Kafka every 5 seconds
uname = ["Ahmad","Sam","Jack","John","Kelly"]
password = ["123543","abcsdq13","fg5fd45","dsdfhtry3","dhtrytry55"]
firstname = ["Ahmad","Sam","Jack","John","Kelly"]
lastname = ["Rolland","Smith","Hilton","Sweed"]
email = ["asdas@g.com","aswqedas@g.com","wer453@g.com","ghfg45@g.com",]
for i in range(1000):
    data = {"username":random.choice(uname)
            ,"password":random.choice(password)
            ,"firstname":random.choice(firstname)
            ,"lastname":random.choice(lastname)
            ,"email":random.choice(email)}
    
    print("sending data")

    producer.send('signup-topic',data)
    time.sleep(5)
