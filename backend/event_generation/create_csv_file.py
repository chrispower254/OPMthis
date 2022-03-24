import csv
import json

def create_csv_file(config):

    #f = open('config.json')
    #f = open(config)
    #config = json.load(f)

    # Define CSV file
    with open('backend/files/events.csv', 'w', newline='') as csv_dump:
        writer = csv.writer(csv_dump,delimiter=';')

        row_init = []
        i=0
        for attribute in config['eventAttributes']:
            if i==0:
                row_init.append("case:concept:name")
            if i==1:
                row_init.append("concept:name")
            if i==2:
                row_init.append("time:timestamp")
            if i>2:
                row_init.append(attribute)
            i+=1

        writer.writerow(row_init)