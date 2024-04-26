import networkx as nx
from student_utils import *

def ptp_solver(G:nx.DiGraph, H:list, alpha:float):
    """
    PTP sovler.
    Input:
        G: a NetworkX graph representing the city.\
        This directed graph is equivalent to an undirected one by construction.
        H: a list of home nodes that you must vist.
        alpha: the coefficient of calculating cost.
    Output:
        tour: a list of nodes traversed by your car.
        pick_up_locs_dict: a dictionary of (pick-up-locations, friends-picked-up) pairs\
        where friends-picked-up is a list/tuple containing friends who get picked up at\
        that sepcific pick-up location. Friends are represented by their home nodes.

    All nodes are reprented as integers.
    
    The tour must begin and end at node 0.
    It can only go through edges that exist in the graph..
    Pick-up locations must be in the tour.
    Everyone should get picked up exactly once
    """

    return tour, pick_up_locs_dict


if __name__ == "__main__":
    pass
