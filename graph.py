import numpy as np
import math
import matplotlib.pyplot as plt
import networkx as nx
from NBody import *
from pylab import *
from starData import *

time = 0 # must be <= 4000

def build_graph(x_coords, y_coords, z_coords):
    graph = nx.Graph()
    if (checkMaximallyPacked == 1):
        planet_list = planet_list_x
    for i in range(len(x_coords)):
        graph.add_node(i, name=planet_list[i], x=x_coords[i][time], y=y_coords[i][time], z=z_coords[i][time])
        for n in graph:
            if n != i:
                nodeA = graph.nodes[n]
                nodeB = graph.nodes[i]

                edge_wt = math.sqrt((nodeA['x'] - nodeB['x'])**2 + (nodeA['y'] - nodeB['y'])**2 + (nodeA['z'] - nodeB['z'])**2)
                # print("edge_wt", edge_wt)
                graph.add_edge(n, i, weight=edge_wt)

    # print out node list
    for node in graph:
        print("NODE ", node, graph.nodes[node])

    nx.draw(graph, with_labels=True)
    plt.draw()
    plt.show()
    tree = nx.minimum_spanning_tree(graph)

    nx.draw(tree, with_labels=True)
    plt.draw()
    plt.show()

if __name__ == '__main__':
    planets,x,y,z,vx,vy,vz,ax,ay,az,m = set_up()
    a,b,c,va,vb,vc,aa,ab,ac,energy, ChangeInE,totalH, ChangeInH,hRatio,hTotalMag, rBary,vBary = nOrbit(x,y,z,x,y,z,vx,vy,vz,vx,vy,vz,G,m,m,N,planets,dt);
    build_graph(a,b,c)
