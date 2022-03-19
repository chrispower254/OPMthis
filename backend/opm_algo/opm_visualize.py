import os
from pm4py.visualization.heuristics_net import visualizer as hn_visualizer

def opm_visualize(type,heu_net):
    if type == 'heu_net':
        gviz = hn_visualizer.apply(heu_net, parameters={hn_visualizer.Variants.PYDOTPLUS.value.Parameters.FORMAT: "png"})
        hn_visualizer.save(gviz,os.path.join('frontend','src','files', 'heunet.png'))