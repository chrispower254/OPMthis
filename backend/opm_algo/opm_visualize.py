import os
from pm4py.visualization.heuristics_net import visualizer as hn_visualizer
from pm4py.visualization.dfg import visualizer as dfg_visualization
from pm4py.visualization.process_tree import visualizer as pt_visualizer


def opm_visualize(type,process_net, event_log):
    # One case for each process net type
    if type == 'heu_net':
        gviz = hn_visualizer.apply(process_net, parameters={hn_visualizer.Variants.PYDOTPLUS.value.Parameters.FORMAT: "png"})
        hn_visualizer.save(gviz,os.path.join('frontend','src','files', 'heunet.png'))
    elif type == 'dfg':
        gviz = dfg_visualization.apply(process_net, log = event_log, variant=dfg_visualization.Variants.FREQUENCY)
        dfg_visualization.save(gviz,os.path.join('frontend','src','files', 'heunet.png'))
    elif type == 'process_tree':
        gviz = pt_visualizer.apply(process_net)
        pt_visualizer.save(gviz,os.path.join('frontend','src','files', 'heunet.png'))
    elif type == 'petri_net':
        print("Not implemented yet")
