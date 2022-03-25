import pandas as pd
import os
from pm4py.objects.conversion.log import converter as log_converter
from pm4py.algo.discovery.heuristics import algorithm as heuristics_miner
from pm4py.util import constants
from pm4py.visualization.heuristics_net import visualizer as hn_visualizer
from datetime import datetime


def update_event_log(current_time):
    log_csv = pd.read_csv(os.path.join('backend','files', 'events-' + current_time + '.csv'), sep=';')
    event_log = log_converter.apply(log_csv, parameters={constants.PARAMETER_CONSTANT_CASEID_KEY: "case:concept:name",
                                                         constants.PARAMETER_CONSTANT_ACTIVITY_KEY: "concept:name",
                                                         constants.PARAMETER_CONSTANT_TIMESTAMP_KEY: "time:timestamp"})
    return event_log


def recompute_heu_net(event_log, dependency):
    heu_net = heuristics_miner.apply_heu(event_log, parameters={
        heuristics_miner.Variants.CLASSIC.value.Parameters.DEPENDENCY_THRESH: dependency})
    return heu_net


def visualize_heu_net(heu_net,current_time):
    gviz = hn_visualizer.apply(heu_net, parameters={hn_visualizer.Variants.PYDOTPLUS.value.Parameters.FORMAT: "png"})
    hn_visualizer.save(gviz,os.path.join('frontend','src','files', 'heunet.png'))


def opm_update(current_time):
    print("test2")
    updated_event_log = update_event_log(current_time)
    heu_net = recompute_heu_net(updated_event_log, 0.01)
    visualize_heu_net(heu_net,current_time)

    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    print("opm_update at: " + current_time)