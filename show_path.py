import networkx as nx
import matplotlib.pyplot as plt

'''
NODE:
d3: y(string)
d4: x(string)
d5: osmid(string)
EDGE:
8: name
9: length
10: osmid
12: oneway
16:geometry
'''
H = nx.read_graphml('manhatten.graphml')
G = nx.Graph(H)
# G = nx.Graph.to_undirected(H,as_view=True)
print(nx.info(H))
print(nx.info(G))

# positional dictionary

xdict = nx.get_node_attributes(G, "x")
ydict = nx.get_node_attributes(G, "y")

ds=[xdict,ydict]
dict={}
for i in xdict.keys():
    dict[i] = tuple( float(dict[i]) for dict in ds)

# print(dict)

nx.draw(G,pos=dict, node_size=10)

plt.show()
