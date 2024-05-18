import networkx as nx
from student_utils import *

def get_sp(G):
    shortest_path = {}

    for from_node in G.nodes:
        for to_node in G.nodes:
            if from_node != to_node:
                path = nx.shortest_path(G, from_node, to_node, 'weight')
                shortest_path[(from_node, to_node)] = path

    return shortest_path

def ptp_solver(G: nx.DiGraph, H: list, alpha: float):
    """
    PTP solver.
    Input:
        G: a NetworkX graph representing the city.
        This directed graph is equivalent to an undirected one by construction.
        H: a list of home nodes that you must visit.
        alpha: the coefficient of calculating cost.
    Output:
        tour: a list of nodes traversed by your car.
        pick_up_locs_dict: a dictionary of (pick-up-locations, friends-picked-up) pairs
        where friends-picked-up is a list/tuple containing friends who get picked up at
        that specific pick-up location. Friends are represented by their home nodes.

    All nodes are represented as integers.

    The tour must begin and end at node 0.
    It can only go through edges that exist in the graph.
    Pick-up locations must be in the tour.
    Everyone should get picked up exactly once.
    """
    d = nx.floyd_warshall(G)
    sp = {a: dict(b) for a, b in d.items()}
    T = [0]

    def d_cost(T):
        driving_cost = 0
        for i in range(0, len(T)-1):
            driving_cost += sp[T[i]][T[i+1]]
        driving_cost += sp[T[-1]][0]
        return driving_cost

    def cost(T):
        c = 0
        for h in H:
            dict_h = sp[h]
            for key in dict_h:
                if key in T:
                    c += dict_h[key]
                    break
        return c + d_cost(T) * alpha

    min_cost = cost(T.copy())
    new_T = T.copy()

    while True:
        for i in range(1, len(G.nodes)):
            if i in T:
                idx = T.index(i)
                T.pop(idx)
                tmp_cost = cost(T.copy())
                if tmp_cost < min_cost:
                    new_T = T.copy()
                    min_cost = tmp_cost
                T.insert(idx, i)
            else:
                min_d = float('inf')
                min_idx = 0
                for idx in range(1, len(T) + 1):
                    T.insert(idx, i)
                    tmp_cost = d_cost(T.copy())
                    if tmp_cost < min_d:
                        min_d = tmp_cost
                        min_idx = idx
                    T.remove(i)
                T.insert(min_idx, i)
                tmp_cost = cost(T.copy())
                if tmp_cost < min_cost:
                    new_T = T.copy()
                    min_cost = tmp_cost
                T.remove(i)
        if T == new_T:
            break
        T = new_T.copy()

    # Transform to answer
    shortest_path = get_sp(G)
    tour = [0]
    T.append(0)
    pick_up_locs_dict = {}
    for i in range(len(T)-1):
        tour += shortest_path[(T[i], T[i+1])][1:]

    for i in set(tour):
        pick_up_locs_dict[i] = []
    for h in H:
        tmp_dict = sp[h]
        for key in tmp_dict:
            if key in tour:
                pick_up_locs_dict[key].append(h)
                break

    return tour, pick_up_locs_dict

if __name__ == "__main__":
    pass