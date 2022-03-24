
from pm4py.statistics.traces.generic.log import case_statistics

def getTroughputTime(event_log):
    median_case_duration = case_statistics.get_median_caseduration(event_log, parameters={
        case_statistics.Parameters.TIMESTAMP_KEY: "time:timestamp"
    })
    return median_case_duration
