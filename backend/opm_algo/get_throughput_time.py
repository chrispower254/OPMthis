
from pm4py.statistics.traces.generic.log import case_statistics

def get_throughput_time(event_log):
    median_case_duration = case_statistics.get_median_case_duration(event_log, parameters={
        case_statistics.Parameters.TIMESTAMP_KEY: "time:timestamp"
    })
    
    return str(median_case_duration)
