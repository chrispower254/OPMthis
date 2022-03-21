from backend.event_generation.create_csv_file import create_csv_file
from backend.event_generation.kafka_consumer import NewKafkaConsumer
from backend.event_generation.kafka_listener import kafka_listener
import json

class CsvLogGenerator:

    def __init__(self):
        f = open('config.json')
        config = json.load(f)

        create_csv_file()

        kafka_consumer = NewKafkaConsumer(config['kafkaSettings']['topic'], config['kafkaSettings']['bootstrapServers']).consumer

        kafka_listener(kafka_consumer)








