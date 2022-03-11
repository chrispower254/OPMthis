from multiprocessing import Process
import run

# Press the green button in the gutter to run the script.
if __name__ == '__main__':

    p1 = Process(target=run.generate_log_main)
    p2 = Process(target=run.opm_update_main)
    p1.start()
    p2.start()
    p1.join()
    p2.join()

    print("End of main")





