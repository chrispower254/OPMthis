from datetime import datetime
from opm_algo.event_log_updater import event_log_updater
from opm_algo.opm_compute import opm_compute
from opm_algo.opm_visualize import opm_visualize

def opm_update(event_log_type, opm_type, process_net_type):
    print("OPM update started")
    updated_event_log = event_log_updater(event_log_type)
    process_net = opm_compute(opm_type, updated_event_log, 0.01)
    opm_visualize(process_net_type,process_net)

    now = datetime.now()
    print("opm_update at: " + now.strftime("%H:%M:%S"))