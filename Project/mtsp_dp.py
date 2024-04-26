import networkx as nx

def mtsp_dp(G):
    """
    TSP solver using dynamic programming.
    Input:
        G: a NetworkX graph representing the city.\
        This directed graph is equivalent to an undirected one by construction.
    Output:
        tour: a list of nodes traversed by your car.

    All nodes are reprented as integers.

    You must solve the problem using dynamic programming.
    
    The tour must begin and end at node 0.
    It can only go through edges that exist in the graph..
    It must visit every node in G exactly once.
    """
    
    return tour