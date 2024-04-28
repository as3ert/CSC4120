import networkx as nx
from mtsp_dp import mtsp_dp
from student_utils import *

def access_edges(G):
    for (u, v, d) in G.edges(data=True):
        print(u, v, d)

def access_nodes(G):
    for n in G.nodes:
        print(n)

def access_floyd_warshall(G):
    d = nx.floyd_warshall(G)
    results = {a: dict(b) for a, b in d.items()}
    print(results)

def pthp_to_tsp(G, H):
    # Create a new TSP graph
    TSP = nx.Graph()
    TSP.add_node(0)
    TSP.add_nodes_from(H)

    # Add edges to TSP
    for from_node in TSP.nodes:
        for to_node in TSP.nodes:
            if from_node != to_node:
                TSP.add_edge(from_node, to_node, weight=nx.shortest_path_length(G, from_node, to_node, 'weight'))
    
    # Optional: Draw the TSP graph
    draw_gragh(TSP)

    return TSP

def pthp_solver_from_tsp(G, H):
    """
    PTHP sovler via reduction to Euclidean TSP.
    Input:
        G: a NetworkX graph representing the city.\
        This directed graph is equivalent to an undirected one by construction.
        H: a list of home nodes that you must vist.
    Output:
        tour: a list of nodes traversed by your car.

    All nodes are reprented as integers.

    You must solve the question by first transforming a PTHP\
    problem to a TSP problem. After solving TSP via the dynammic\
    programming algorithm introduced in lectures, construct a solution\
    for the original PTHP problem.
    
    The tour must begin and end at node 0.
    It can only go through edges that exist in the graph..
    It must visit every node in H.
    """
    draw_gragh(G)

    TSP = pthp_to_tsp(G, H)

    return
    
    # reduction

    tsp_tour = mtsp_dp(reduced_graph)

    # reduction

    return tour


if __name__ == "__main__":
    pass