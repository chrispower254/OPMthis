from datetime import datetime
from opm_algo.event_log_updater import event_log_updater
from opm_algo.opm_compute import opm_compute
from opm_algo.opm_visualize import opm_visualize
from opm_algo.get_throughput_time import getTroughputTime
from multiprocessing import Queue

def opm_update(config, return_dict):
    print("OPM update started")
    event_log_type = config["opmSettings"]["eventLogType"]
    opm_type = config["opmSettings"]["opmAlgo"]
    process_net_type = config["opmSettings"]["processNetType"]
    heu_min_dependency = float(config["opmSettings"]["heuMinConfig"]["dependency"])
    print(heu_min_dependency)

    updated_event_log = event_log_updater(event_log_type)
    process_net = opm_compute(opm_type, updated_event_log, heu_min_dependency)
    opm_visualize(process_net_type,process_net,updated_event_log)
    return_dict[0] = getTroughputTime(updated_event_log)

    now = datetime.now()
    print("opm_update at: " + now.strftime("%H:%M:%S"))