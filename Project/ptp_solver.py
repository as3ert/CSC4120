import networkx as nx
from student_utils import *

def calculate_cost(T, G, alpha, H):
    """
    Calculate the total cost of the tour including driving and walking costs.
    Parameters:
        T (list): The list of nodes representing the current tour.
        G (nx.Graph): The graph representing all nodes and edges with their weights.
        alpha (float): Coefficient for the driving cost.
        H (list): List of home nodes.
        pick_up_locs_dict (dict): Dictionary mapping each home node to its nearest pickup point in the tour.
    Returns:
        float: Total cost of the tour.
    """
    # Initialize driving and walking costs
    driving_cost = 0
    walking_cost = 0

    # Calculate driving cost by summing the weights of the edges in the tour
    # print(T)
    for u, v in zip(T[:-1], T[1:]):
        # print(u, v)
        driving_cost += G[u][v]['weight']
    
    # Calculate walking cost for each friend from their home to their pickup location
    for home in H:
        nearest_pickup, length = get_nearest_pickup(home, T, G)
        if home in G and nearest_pickup in G:
            walking_cost += length

    # Total cost includes both driving and walking costs
    total_cost = alpha * driving_cost + walking_cost
    return total_cost

def get_nearest_pickup(home, tour, G):
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
    shortest_distance = float('inf')
    nearest_node = None

    # Iterate over each node in the tour to find the closest one to the given home node
    for node in tour:
        if G.has_node(home) and G.has_node(node):
            try:
                # Calculate the shortest path distance from the home node to the current node in the tour
                distance = nx.shortest_path_length(G, source=home, target=node, weight='weight')
                # If this distance is shorter than the previously found distances, update the nearest node and distance
                if distance < shortest_distance:
                    shortest_distance = distance
                    nearest_node = node
            except nx.NetworkXNoPath:
                # If no path exists between the home and the node, continue to the next node
                continue

    return (nearest_node, shortest_distance)

def ptp_solver(G, H, alpha):
    # draw_gragh(G)

    T = [0, 0]  # Start with the starting node
    pick_up_locs_dict = {}
    best_cost = float('inf')

    improved = True
    while improved:
        improved = False
        # Try removing nodes
        for i in range(1, len(T) - 1):
            if T[i] in H:
                continue  # Don't remove a home node
            shortest_path = nx.shortest_path(G, T[i - 1], T[i + 1], 'weight')[1:-1]
            if (len(shortest_path) == 0):
                new_T = T[:i] + T[i + 2:]
            else:
                new_T = T[:i] + shortest_path + T[i + 1:]
            new_cost = calculate_cost(new_T, G, alpha, H)
            if new_cost < best_cost:
                best_cost = new_cost
                best_T = new_T
                improved = True

        # Try adding nodes
        for node in set(G.nodes()) - set(T):
            for i in range(1, len(T)):
                shortest_path_from = nx.shortest_path(G, T[i - 1], node, 'weight')[1:]
                shortest_path_to = nx.shortest_path(G, node, T[i], 'weight')[1:-1]
                shortest_path = shortest_path_from + shortest_path_to
                new_T = T[:i] + shortest_path + T[i:]
                new_cost = calculate_cost(new_T, G, alpha, H)
                if new_cost < best_cost:
                    best_cost = new_cost
                    best_T = new_T
                    improved = True

        T = best_T if improved else T

    # Restore T if T is [0, 0]
    if T == [0, 0]:
        T = [0]

    # Update pick-up locations after finalizing T
    for home in H:
        nearest_node, _ = get_nearest_pickup(home, T, G)
        try:
            pick_up_locs_dict[nearest_node].append(home)
        except KeyError:
            pick_up_locs_dict[nearest_node] = [home]

    return T, pick_up_locs_dict

if __name__ == "__main__":
    # Assuming the graph G and homes H have been properly initialized
    pass
