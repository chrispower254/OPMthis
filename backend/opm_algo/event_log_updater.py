import pandas as pd
import os
from pm4py.objects.conversion.log import converter as log_converter
from pm4py.util import constants
from pm4py.algo.filtering.pandas.attributes import attributes_filter
import json
import pm4py

def event_log_updater(type):
    f = open('config.json')
    config = json.load(f)

    if type == 'csv':
        #cwd = os.getcwd()  # Get the current working directory (cwd)
        #files = os.listdir(cwd)  # Get all the files in that directory
        #print("Files in %r: %s" % (cwd, files))
        log_csv = pd.read_csv(os.path.join('backend','files', 'events.csv'), sep=';')
        event_log = log_converter.apply(log_csv, parameters={constants.PARAMETER_CONSTANT_CASEID_KEY: "case:concept:name",
                                                             constants.PARAMETER_CONSTANT_ACTIVITY_KEY: "concept:name",
                                                             constants.PARAMETER_CONSTANT_TIMESTAMP_KEY: "time:timestamp"})

        event_log_filtered = event_log
        for attribute in config['filters']:
            key_arr = config['filters'][attribute]
            event_log_filtered = pm4py.filter_event_attribute_values(event_log_filtered, attribute, key_arr,level='event')

    if type == 'xes':
        event_log = 'lol nuffing'
        event_log_filtered = event_log
        for attribute in config['filters']:
            key_arr = config['filters'][attribute]
            event_log_filtered = pm4py.filter_event_attribute_values(event_log_filtered, attribute, key_arr,level='event')

    return event_log_filtered