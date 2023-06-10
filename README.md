# Kafka_Producer_Consumer_to_SQL_Project
Creating a Kafka producer.py, consumer.py &amp; PgAdmin SQL DB

# Required installations if not existing on the same environment:
pip install kafka-python
conda install -c conda-forge kafka-python 
conda install -c anaconda sqlalchemy
conda install -c anaconda psycopg2

# What the project about:
- Created Upstash account
- Created New single replica Cluster
- producer.py Python base code 

![KafkaProducer_upstash](https://github.com/hanydief/Kafka_Producer_Consumer_to_SQL_Project/blob/main/Outputs/KafkaProducer_upstash.png)

- On VS created a producer.py to publish random message to Kafka every 5 seconds

![kafkaProducer_VS](https://github.com/hanydief/Kafka_Producer_Consumer_to_SQL_Project/blob/main/Outputs/kafkaProducer_VS.png)

- consumer.py Python base code 
- 
![KafkaConsumer_upstash](https://github.com/hanydief/Kafka_Producer_Consumer_to_SQL_Project/blob/main/Outputs/KafkaConsumer_upstash.png)

- On VS created a consumer.py to fitch the producer.py random messages from Kafka every 2 seconds

![kafkaConsumer_VS](https://github.com/hanydief/Kafka_Producer_Consumer_to_SQL_Project/blob/main/Outputs/kafkaConsumer_VS.png)

- After activating the environment: $ conda activate kafka-env
- On GitBash: $ python producer.py 

![kafkaProducer_GitBash](https://github.com/hanydief/Kafka_Producer_Consumer_to_SQL_Project/blob/main/Outputs/kafkaProducer_GitBash.png)

- After activating the environment: $ conda activate kafka-env
- On GitBash: $ python consumer.py 

![kafkaConsumer_GitBash](https://github.com/hanydief/Kafka_Producer_Consumer_to_SQL_Project/blob/main/Outputs/kafkaConsumer_GitBash.png)

- using engine Pushing all produced data thru consumer.py to PgAdmin SQL Database

![kafkaConsumer_PGAdmin_SQL](https://github.com/hanydief/Kafka_Producer_Consumer_to_SQL_Project/blob/main/Outputs/kafkaConsumer_PGAdmin_SQL.png)


# Benificial links:
https://upstash.com/?gclid=CjwKCAjwvpCkBhB4EiwAujULMu611BMTjPj1328j0xQ8lKUNu55HbCBBtwRG8ysGnVgpFEML33sTRxoCWcMQAvD_BwE
https://pypi.org/project/psycopg2-binary/
