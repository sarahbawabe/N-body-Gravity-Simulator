import numpy as np
import math
import matplotlib.pyplot as plt
import networkx as nx
from NBody import *
from pylab import *
from starData import *


a,b,c,va,vb,vc,aa,ab,ac,energy, ChangeInE,totalH, ChangeInH,hRatio,hTotalMag, rBary,vBary = nOrbit(x,y,z,x,y,z,vx,vy,vz,vx,vy,vz,G,m,m,N,planets,dt);

# a,b,c,va,vb,vc,aa,ab,ac,energy, ChangeInE,totalH, ChangeInH,hRatio,hTotalMag, rBary,vBary = nOrbit(NBody.x,NBody.y,NBody.z,NBody.x,NBody.y,NBody.z,NBody.vx,NBody.vy,NBody.vz,NBody.vx,NBody.vy,NBody.vz,NBody.G,NBody.m,NBody.m,NBody.N,NBody.planets,NBody.dt);

print("a[0]", a[0])
# a shape: (10, 4001)
print("a shape", len(a), len(a[0]))
print("b shape", len(b), len(b[0]))
print("c shape", len(c), len(c[0]))

print("va shape", len(va), len(va[0]))
print("va[0]", va[0])

# aa shape 10 4000
print("aa shape", len(aa), len(aa[0]))
print("aa[0]", aa[0])

nodes = [a,b,c]
print("nodes shape", len(nodes), len(nodes[0]), len(nodes[0][0]))

# build a graph
def build_graph(x_coords, y_coords, z_coords):
    graph = nx.Graph()
    for i in range(len(x_coords)):
        graph.add_node(i, x=x_coords[i][0], y=y_coords[i][0], z=z_coords[i][0])
        for n in graph:
            if n != i:
                nodeA = graph.nodes[n]
                nodeB = graph.nodes[i]
                # print("nodeA", nodeA)
                # x_diff = (nodeA['x'] - nodeB['x'])**2
                # print(x_diff)
                edge_wt = math.sqrt((nodeA['x'] - nodeB['x'])**2 + (nodeA['y'] - nodeB['y'])**2 + (nodeA['z'] - nodeB['z'])**2)
                # print("edge_wt", edge_wt)
                graph.add_edge(n, i, weight=edge_wt)

    # print(graph.adj)
    nx.draw(graph)
    plt.draw()
    plt.show()
    tree = nx.minimum_spanning_tree(graph)
    # print(tree.adj)
    nx.draw(tree)
    plt.draw()
    plt.show()

if __name__ == '__main__':
    build_graph(a,b,c)
