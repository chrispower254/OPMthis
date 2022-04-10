from multiprocessing import Process
import api.flask_server as flask_server
from event_generation.generate_csv_log import CsvLogGenerator
import json
from runAdidas import sendPost

if __name__ == '__main__':
    print("Start of main")
    # Either use 'kafka' or 'adidas'
    # 'adidas' uses a fake event log for stream generation
    source = "adidas"

    # Multiprocessing needed in order to listen to events and run the API simultaneously
    if source == "kafka":
        f = open('config.json')
        config = json.load(f)
        p1 = Process(target=CsvLogGenerator,args=(config,source))
        p2 = Process(target=flask_server.app_run,args=([source]))
        p1.start()
        p2.start()
        p1.join()
        p2.join()
    elif source == "adidas":
        f = open('configAdidas.json')
        config = json.load(f)
        p1 = Process(target=CsvLogGenerator,args=(config,source))
        p2 = Process(target=flask_server.app_run,args=([source]))
        p3 = Process(target=sendPost)
        p1.start()
        p2.start()
        p3.start()
        p1.join()
        p2.join()
        p3.join()
    
    print("End of main")
