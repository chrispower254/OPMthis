from event_generation.create_csv_file import create_csv_file
from event_generation.kafka_consumer import NewKafkaConsumer
from event_generation.kafka_listener import kafka_listener


class CsvLogGenerator:

    def __init__(self,current_time):
        self.current_time = current_time

        create_csv_file(current_time)

        kafka_consumer = NewKafkaConsumer('schlaegerbande_events', 'localhost:9092').consumer

        kafka_listener(current_time,kafka_consumer)









