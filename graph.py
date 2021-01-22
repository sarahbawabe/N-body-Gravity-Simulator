import numpy as np
import math
import matplotlib.pyplot as plt
import networkx as nx
from NBody import *
from pylab import *
from starData import *


a,b,c,va,vb,vc,aa,ab,ac,energy, ChangeInE,totalH, ChangeInH,hRatio,hTotalMag, rBary,vBary = nOrbit(x,y,z,x,y,z,vx,vy,vz,vx,vy,vz,G,m,m,N,planets,dt);

# a,b,c,va,vb,vc,aa,ab,ac,energy, ChangeInE,totalH, ChangeInH,hRatio,hTotalMag, rBary,vBary = nOrbit(NBody.x,NBody.y,NBody.z,NBody.x,NBody.y,NBody.z,NBody.vx,NBody.vy,NBody.vz,NBody.vx,NBody.vy,NBody.vz,NBody.G,NBody.m,NBody.m,NBody.N,NBody.planets,NBody.dt);

print("a", a)
# build a graph
graph = nx.Graph()
