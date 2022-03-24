import csv
import json
import re

def kafka_listener(consumer, config):

    print("listener is running")
    #f = open('config.json')
    #f = open(config_string)
    #config = json.load(f)

    for msg in consumer:
        print("listener received message")
        # Get actual payload from message and split to work with csv.writer
        event_json = json.loads(msg.value.decode('utf-8'))
        payload =""

        print()
        for attribute in config['eventAttributes']:
            if payload != "":
                payload += ","
            if attribute == "event":
                payload += re.search(config['baseUrl'] + '(.*)', event_json[attribute]).group(1)
            if attribute != "event":
                payload += str(event_json[attribute])

        # Append to CSV file
        with open('backend/files/events.csv', 'a', newline='') as csv_dump:
            writer = csv.writer(csv_dump, delimiter=';')
            writer.writerow(payload.split(","))
            print(payload)

    print("Consumer closed")