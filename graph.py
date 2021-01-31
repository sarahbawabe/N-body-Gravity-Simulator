import numpy as np
import math
import matplotlib.pyplot as plt
import networkx as nx
from newNBody import *
from pylab import *
from starData import *
import bodyObject as bOb


def build_graph(x_coords, y_coords, z_coords, time):
    graph = nx.Graph()
    # if (checkMaximallyPacked == 1):
    #     planet_list = planet_list_x
    for i in range(len(x_coords)):
        # name=planet_list[i]
        graph.add_node(i, x=x_coords[i][time], y=y_coords[i][time], z=z_coords[i][time])
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
    # obj_list = bOb.convert_to_obj_list(m, coords_matrix, vels_matrix)
    obj_list = bOb.generate_rand_obj_list(N=10,ndim=3)
    nBody = NBody(obj_list, ndim=3, iters=10)
    nBody.perform_simulation()
    nBody.plot()
    build_graph(nBody.pos_matrix[:,0,:],nBody.pos_matrix[:,1,:],nBody.pos_matrix[:,2,:],9)
