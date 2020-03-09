import networkx as nx
import matplotlib.pyplot as plt

romania_map = {'Arad': {'Sibiu': {'weight': 140}, 'Timisoara': {'weight': 118}, 'Zerind': {'weight': 75}},
               'Bucharest': {'Fagaras': {'weight': 211}, 'Giurgiu': {'weight': 90}, 'Pitesti': {'weight': 101},
                             'Urziceni': {'weight': 85}},
               'Craiova': {'Drobeta': {'weight': 120}, 'Pitesti': {'weight': 138}, 'Rimnicu': {'weight': 146}},
               'Drobeta': {'Mehadia': {'weight': 75}},
               'Eforie': {'Hirsova': {'weight': 86}},
               'Fagaras': {'Sibiu': {'weight': 99}},
               'Hirsova': {'Urziceni': {'weight': 98}},
               'Iasi': {'Neamt': {'weight': 87}, 'Vaslui': {'weight': 92}},
               'Lugoj': {'Mehadia': {'weight': 70}, 'Timisoara': {'weight': 111}},
               'Oradea': {'Sibiu': {'weight': 151}, 'Zerind': {'weight': 71}},
               'Pitesti': {'Rimnicu': {'weight': 97}},
               'Rimnicu': {'Sibiu': {'weight': 80}},
               'Urziceni': {'Vaslui': {'weight': 142}}}

romania_graph = nx.from_dict_of_dicts(romania_map)
print(nx.shortest_path(romania_graph, 'Arad', 'Sibiu'))
print(nx.dijkstra_path(romania_graph, 'Arad', 'Sibiu'))
print(nx.astar.astar_path(romania_graph, 'Arad', 'Sibiu'))
print(nx.astar.astar_path_length(romania_graph, 'Arad', 'Sibiu'))


def distance(a, b):
    (x1, y1) = a
    (x2, y2) = b
    return ((x1 - x1) ** 2 + (y1 - y2) ** 2) * .5


G = nx.grid_graph(dim=[3, 4])
nx.draw(G, with_labels=True, node_color='Red', node_size=100, alpha=0.5)
plt.show(block=True)
print(nx.astar_path(G, (0, 0), (3, 2), distance))
