from multiprocessing import Process
import api.flask_server as api_start
from event_generation.generate_csv_log import CsvLogGenerator

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print("Start of main")

    p1 = Process(target=CsvLogGenerator)
    p2 = Process(target=api_start.app_run)
    p1.start()
    p2.start()
    p1.join()
    p2.join()

    print("End of main")





