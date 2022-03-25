import os
from pm4py.visualization.heuristics_net import visualizer as hn_visualizer
from pm4py.visualization.dfg import visualizer as dfg_visualization

def opm_visualize(type,heu_net, event_log):
    if type == 'heu_net':
        gviz = hn_visualizer.apply(heu_net, parameters={hn_visualizer.Variants.PYDOTPLUS.value.Parameters.FORMAT: "png"})
        hn_visualizer.save(gviz,os.path.join('frontend','src','files', 'heunet.png'))
    if type == 'dfg':
        gviz = dfg_visualization.apply(heu_net, log = event_log, variant=dfg_visualization.Variants.FREQUENCY)
        print("test")
        dfg_visualization.save(gviz,os.path.join('frontend','src','files', 'heunet.png'))