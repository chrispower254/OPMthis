import pandas as pd
import os
from pm4py.objects.conversion.log import converter as log_converter
from pm4py.util import constants

def event_log_updater(type):
    if type == 'csv':
        #cwd = os.getcwd()  # Get the current working directory (cwd)
        #files = os.listdir(cwd)  # Get all the files in that directory
        #print("Files in %r: %s" % (cwd, files))
        log_csv = pd.read_csv(os.path.join('backend','files', 'events.csv'), sep=';')
        event_log = log_converter.apply(log_csv, parameters={constants.PARAMETER_CONSTANT_CASEID_KEY: "case:concept:name",
                                                             constants.PARAMETER_CONSTANT_ACTIVITY_KEY: "concept:name",
                                                             constants.PARAMETER_CONSTANT_TIMESTAMP_KEY: "time:timestamp"})
    if type == 'xes':
        event_log = 'lol nuffing'

    return event_log