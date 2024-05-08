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
    memo = {}
    def dp(v, S):
        if len(S) == 0:
            memo[(v, S)] = (G.edges[0,v]['weight'], 0)
            return memo[(v, S)]
        if (v, S) in memo:
            return memo[(v, S)]
        min = float('inf')
        for i in range(len(S)):
            tmp = G.edges[S[i],v]['weight'] + dp(S[i], S[:i] + S[i+1:])[0]
            if tmp < min:
                min = tmp
                pre=S[i]
        memo[(v, S)] = (min, pre)
        return memo[(v, S)]
    tour = [0]
    S = sorted(G.nodes())
    S.remove(0)
    min = float('inf')
    pre = 0
    for i in range(len(S)):
        tmp = G.edges[S[i],0]['weight'] + dp(S[i], tuple(S[:i] + S[i+1:]))[0]
        if tmp < min:
            min = tmp
            pre = S[i]
    while(len(S) > 0):
        tour.append(pre)
        S.remove(pre)
        print(pre)
        pre = dp(pre, tuple(S))[1]
    tour.append(0)
    tour.reverse()
    
    return tour