import csv
import json
import re

def kafka_listener(consumer):

    print("listener is running")
    f = open('config.json')
    config = json.load(f)

    for msg in consumer:
        print("listener received message")
        # Get actual payload from message and split to work with csv.writer
        event_json = json.loads(msg.value.decode('utf-8'))
        payload = event_json["case"] + "," + re.search(config['baseUrl'] + '(.*)',event_json["event"]).group(1) + "," + event_json["timestamp"]

        # Append to CSV file
        with open('backend/files/events.csv', 'a', newline='') as csv_dump:
            writer = csv.writer(csv_dump, delimiter=';')
            writer.writerow(payload.split(","))
            print(payload)

    print("Consumer closed")