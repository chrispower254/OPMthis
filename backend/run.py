from event_generation.generate_csv_log import CsvLogGenerator
from datetime import datetime
from backend.api.flask_server import app_run


now = datetime.now()
current_time = now.strftime("%Y_%m_%d-%H_%M_%S")

def generate_log_main():
    print("generate_log_main")
    CsvLogGenerator()

