from kafka import KafkaConsumer


class NewKafkaConsumer ():
    def __init__(self, topic, server):
        self.topic = topic
        self.server = server
        self.consumer = KafkaConsumer(
            self.topic, # eg: schlaegerbande_events
            bootstrap_servers= self.server, # eg: bootstrap_servers=['localhost:9092'],
            api_version=(0, 10, 2)
        )
