import pandas as pd
import os
from pm4py.objects.conversion.log import converter as log_converter
from pm4py.util import constants
import pm4py

def event_log_updater(type,filters):

    # Currently only CSV log implemented
    if type == 'csv':
        # Read csv log
        log_csv = pd.read_csv(os.path.join('backend','files', 'events.csv'), sep=';')
        # Timestamp needs to be of type timestamp in order for filtering to work
        log_csv["time:timestamp"] = pd.to_datetime(log_csv["time:timestamp"])
        event_log = log_converter.apply(log_csv, parameters={constants.PARAMETER_CONSTANT_CASEID_KEY: "case:concept:name",
                                                             constants.PARAMETER_CONSTANT_ACTIVITY_KEY: "concept:name",
                                                             constants.PARAMETER_CONSTANT_TIMESTAMP_KEY: "time:timestamp"})
        # Instantiate filtered event log
        event_log_filtered = event_log
        # Iterate through all filters
        for attribute in filters:
            key_arr = filters[attribute]
            if key_arr[0] != "":
                event_log_filtered = pm4py.filter_event_attribute_values(event_log_filtered, attribute, key_arr,level='event')


    return event_log_filtered