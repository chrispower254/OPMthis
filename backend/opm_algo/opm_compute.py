from pm4py.algo.discovery.heuristics import algorithm as heuristics_miner
from pm4py.algo.discovery.dfg import algorithm as dfg_discovery
from pm4py.algo.discovery.inductive import algorithm as inductive_miner


def opm_compute(type,event_log, dependency):
    # Case for each type of OPM algo
    if type == 'heu_min':
        # Dependency only needed for heuristic miner
        heu_min = heuristics_miner.apply_heu(event_log, parameters={
            heuristics_miner.Variants.CLASSIC.value.Parameters.DEPENDENCY_THRESH: dependency})
        return heu_min
    elif type == 'dfg':
        dfg = dfg_discovery.apply(event_log, variant=dfg_discovery.Variants.PERFORMANCE)
        return dfg
    elif type == 'inductive':
        inductive = inductive_miner.apply_tree(event_log)
        return inductive
