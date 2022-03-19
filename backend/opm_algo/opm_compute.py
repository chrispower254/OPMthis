from pm4py.algo.discovery.heuristics import algorithm as heuristics_miner

def opm_compute(type,event_log, dependency):
    if type == 'heu_min':
        heu_net = heuristics_miner.apply_heu(event_log, parameters={
            heuristics_miner.Variants.CLASSIC.value.Parameters.DEPENDENCY_THRESH: dependency})
        return heu_net
