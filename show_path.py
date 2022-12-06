import time
import warnings
import networkx as nx
import matplotlib.pyplot as plt
from algorithms1 import tree
from networkx.algorithms import tree

def init():
    
    """
    Initialise Variables used for the code

    Possible Values
    ----------
    graphsize : 'small', 'large'

    algorithm : 'none', 'kruskal', 'prim', 'both'
        'none' Generate the graph passed in the dataset.
        'kruskal' Implements Kruskal's algorithm to generate and show minimum spanning tree and print running time in console
        'prim' Implements Prim's algorithm to generate and show minimum spanning tree and print running time in console
        'both' Will NOT generate graphs:  only runtime-comparative values printed in console

    node_size : float
        Recommended 3 for 'small' graphsize, 0.5 for 'large' graphsize
    """
    
    graphsize = 'large' 
    algorithm = 'both' 
    node_size = 3 

    return graphsize, algorithm, node_size

def import_dataset(size):
    """
    Import dataset in Graphml format.according to the values initialised
    Parameters
    ----------
    size : string
        Size of dataset to be used
    """
    if size == 'small':
        dataset = 'manhatten.graphml'
    elif size == 'large':
        dataset = 'newyork.graphml'
    else:
        return None
    return nx.read_graphml(dataset)


def make_undirected(graph):
    G = nx.Graph.to_undirected(graph, as_view=True)
    return G

def set_node_position(graph):
    # positional dictionary
    xdict = nx.get_node_attributes(graph, "x")
    ydict = nx.get_node_attributes(graph, "y")

    ds=[xdict,ydict]
    dict={}
    for i in xdict.keys():
        dict[i] = tuple( float(dict[i]) for dict in ds)
    return dict

def make_graph_ds(data):
    return nx.Graph(data)

def draw_graph(data, algorithm):
    global graph_initialised
    global pos
    global node_size
    G = make_graph_ds(data)
    warnings.filterwarnings("ignore")
    print(f"\n{nx.info(G)}")
    if algorithm == 'none':
        pos = set_node_position(G)
        make_undirected(G)
        nx.draw(G,pos=pos, node_size=node_size)
        return None
    else:
        if graph_initialised is True:
            nx.draw(G,pos=pos, node_size=node_size)
            return None
        else:
            pos = set_node_position(G)
            graph_initialised = True
            return G

def do_algo(graph, algorithm):
        start = time.time()
        mst = tree.minimum_spanning_edges(graph, algorithm=algorithm, weight='d9', keys=True, data=True, ignore_nan=False)
        end = time.time()
        mst = list(mst)
        time_taken = (end-start) * 10**3 #time in ms

        draw_graph(mst, algorithm)
        print(f"Algorithm: {algorithm}\nTime taken: {time_taken:.03f}ms")

def do_algo1(graph, algorithm):
        global now
        start = now
        start1 = time.time()
        mst = tree.minimum_spanning_edges(graph, algorithm=algorithm, weight='d9', keys=True, data=True, ignore_nan=False)
        mst = list(mst)
        end = time.time()
        time_taken = (end-start) * 10**3 #time in ms

        draw_graph(mst, algorithm)
        print(f"Algorithm: {algorithm}\nTime taken: {time_taken:.03f}ms")
        now = start + start1 - end

def implement_algo(algorithm, size):
    runs = 1
    data = import_dataset(size)
    graph = draw_graph(data, algorithm)
    if algorithm != 'kruskal' and algorithm != 'prim' and algorithm != 'both':
        return None
    if algorithm == 'both':
        runs = 2
    for i in range(runs):
        if algorithm == 'prim' or algorithm == 'both':
            algorithm = 'prim'
            do_algo(graph, algorithm)
            algorithm = 'kruskal'
        else:
            do_algo(graph, algorithm)


if __name__ == "__main__":
    now = time.time()
    graphsize, algorithm, node_size = init()
    graph_initialised = False
    pos = {}
    implement_algo(algorithm, graphsize)
    if algorithm != 'both':
        plt.show()