import networkx as nx

G = {
    'a': {'b': 3, 'd': 1},
    'b': {'a': 3, 'c': 2},
    'c': {'b': 3, 'f': 5},
    'd': {'a': 1, 'e': 8, 'f': 12},
    'e': {'d': 8, 'f': 4},
    'f': {'c': 5, 'd': 12, 'e': 4}
}


def setup_dijkstra(start):
    D = {start: 0}
    P = {}
    Q = [(0, start)]
    S = set()


def relax_dijkstra(G, start, neighbor, D, P):
    inf = float('inf')
    d = D.get(start, inf) + G[start][neighbor]
    if d < D.get(neighbor, inf):
        D[neighbor], P[neighbor] = d, start
        print(D, P)
        return True


P = {}
for outer_counter, u in enumerate(G):
    for inner_counter, v in enumerate(G[u]):
        relax_dijkstra(G, u, v, {u: 0}, P)
