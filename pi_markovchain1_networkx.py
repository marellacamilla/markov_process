import networkx as nx
import numpy as np
from numpy.linalg import inv
import pandas as pd
import matplotlib.pyplot as plt

G = nx.MultiDiGraph()
G.add_node(0)
G.add_node(1)
G.add_node(2)

G.add_edge(0,1, weight=2)
G.add_edge(1,0)
G.add_edge(2,1, weight=3)
G.add_edge(0,2)
G.add_edge(0,0)
G.add_edge(2,2)
G.add_edge(1,1) 

S= nx.stochastic_graph(G)
print('Right-stochastic representation of directed graph G.')
print(S)


M= nx.to_numpy_matrix(S, nodelist=[0,1,2])
print('The adjacent matrix M is:')
print(M)

M = np.array(M, dtype=np.float64)
#Let's evaluate the degree matrix D

D = np.diag(np.sum(M, axis=0))
print('The diagonal matrix D is:')
print(D)
#..the transition matrix T
T = np.dot(inv(D), M)
print('The transition matrix T is:')
print(T)

# let's define the random walk length
walkLength = 10
# define the starting node, say the 0-th
p = np.array([[1.0, 0.0, 0.0]])
stateHist=p
visited = list()
for k in range(walkLength):
    # evaluate the next state vector
    p = np.dot(p,T)
    print(p)
    stateHist=np.append(stateHist,p,axis=0)
    dfDistrHist = pd.DataFrame(stateHist)
dfDistrHist.plot()
plt.show()





