from event_generation.create_csv_file import create_csv_file
from event_generation.kafka_consumer import NewKafkaConsumer
from event_generation.kafka_listener import KafkaListener

class CsvLogGenerator:

    def __init__(self,config,source):

        create_csv_file(config)

        kafka_consumer = NewKafkaConsumer(config['kafkaSettings']['topic'], config['kafkaSettings']['bootstrapServers']).consumer
        print("Kafka Consumer listening for topic \'" + config['kafkaSettings']['topic'] + "\' on host " + config['kafkaSettings']['bootstrapServers'])
        kafka_listener = KafkaListener(kafka_consumer,config)
        kafka_listener.listen()








