import pandas as pd
import json
import time 
import requests

filepath = '/Users/christophschroeder/PycharmProjects/OPMthis/backend/files/adidas.csv'
url = 'http://localhost:8082/topics/adidas'
headers = {'content-type': 'application/vnd.kafka.json.v2+json'}

def sendPost():
    df = pd.read_csv(filepath, delimiter=';')
    
    for index, row in df.iterrows(): 
        json_dict = {
            "case": row[0],
            "event": row[1],
            "timestamp": row[2],
            "device_type": row[3],
            "country": row[4],
            "continent": row[5],
            "city": row[6],
        }
        json_raw = json.dumps(json_dict)
        data = '{"records":[{"value":'+ json_raw + '}]}';
        r = requests.post(url, data=data, headers=headers)
        time.sleep(5)

