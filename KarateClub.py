import networkx as nx
import matplotlib.pyplot as plt 

#Let's import the ZKC graph:
ZKC_graph = nx.karate_club_graph()

#Let's keep track of which nodes represent John A and Mr Hi
Mr_Hi = 0
John_A = 33

#Let's display the labels of which club each member ended up joining
club_labels = nx.get_node_attributes(ZKC_graph,'club')

#just show a couple of the labels
print({key:club_labels[key] for key in range(10,16)})

A = nx.convert_matrix.to_numpy_matrix(ZKC_graph)
circ_pos = nx.circular_layout(ZKC_graph) 

#Use the networkx draw function to easily visualise the graph
nx.draw(ZKC_graph,circ_pos)

#let's highlight Mr Hi (green) and John A (red)
nx.draw_networkx_nodes(ZKC_graph, circ_pos, nodelist=[Mr_Hi], node_color='g', alpha=1)
nx.draw_networkx_nodes(ZKC_graph, circ_pos, nodelist=[John_A], node_color='r', alpha=1)

#how many edges are present compared to the total possible number of edges
density = nx.density(ZKC_graph)

print('The edge density is: ' + str(density))

#the most important nodes, mostly connected to lots of other nodes
degree = ZKC_graph.degree()

degree_list = []

for (n,d) in degree:
    degree_list.append(d)

av_degree = sum(degree_list) / len(degree_list)

print('The average degree is ' + str(av_degree))