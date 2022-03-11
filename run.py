from event_generation.generate_csv_log import CsvLogGenerator
from opm_algo.sliding_window import opm_update
from datetime import datetime
import time


now = datetime.now()
current_time = now.strftime("%Y_%m_%d-%H_%M_%S")

def generate_log_main():
    print("generate_log_main")
    CsvLogGenerator(current_time)

def opm_update_main():
    while True:
        time.sleep(10)
        opm_update(current_time)
        print("opm_update at: " + current_time)

