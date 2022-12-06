from heapq import heappop, heappush
from itertools import count
from operator import itemgetter
from networkx.utils import UnionFind

def kruskal_mst_edges(G, weight="weight"):
    """
    Iterate over edge of a Kruskal's algorithm 

    Parameters
    ----------
    G : NetworkX Graph
        The graph holding the tree of interest.

    weight : string (default: 'weight')
        The name of the edge attribute holding the edge weights.
    """
    subtrees = UnionFind()
    edges = G.edges(data=True)

    included_edges = []
    open_edges = []
    for e in edges:
        d = e[-1]
        wt = d.get(weight, 1)

        edge = (wt,) + e
        open_edges.append(edge)

    sorted_open_edges = sorted(open_edges, key=itemgetter(0))

    # Condense the lists into one
    included_edges.extend(sorted_open_edges)
    sorted_edges = included_edges
    del open_edges, sorted_open_edges, included_edges

    for wt, u, v, d in sorted_edges:
        if subtrees[u] != subtrees[v]:
            yield u, v, d
            subtrees.union(u, v)


def prim_mst_edges(G, weight="weight"):
    """
    Iterate over edges of Prim's algorithm

    Parameters
    ----------
    G : NetworkX Graph
        The graph holding the tree of interest.

    weight : string (default: 'weight')
        The name of the edge attribute holding the edge weights.
    """
    push = heappush
    pop = heappop

    nodes = set(G)
    c = count()

    while nodes:
        u = nodes.pop()
        frontier = []
        visited = {u}

        for v, d in G.adj[u].items():
            wt = d.get(weight, 1) 
            push(frontier, (wt, next(c), u, v, d))
        while nodes and frontier:
            W, _, u, v, d = pop(frontier)
            if v in visited or v not in nodes:
                continue
            yield u, v, d

            # update frontier
            visited.add(v)
            nodes.discard(v)

            for w, d2 in G.adj[v].items():
                if w in visited:
                    continue
                new_weight = d2.get(weight, 1) 
                push(frontier, (new_weight, next(c), v, w, d2))

ALGORITHMS = {
    "kruskal": kruskal_mst_edges,
    "prim": prim_mst_edges
}

def minimum_spanning_edges(G, algorithm="kruskal", weight="weight"):
    algo = ALGORITHMS[algorithm]
    return algo(G, weight=weight)