import networkx as nx
import pandas as pd
import matplotlib.pyplot as plt

# print(dir(nx))
# print(dir(pd))
# print(help(nx.all_shortest_paths))
ans_1 = {
    'A': ['B', 'G', 'H'],
    'B': ['A', 'D', 'C'],
    'C': ['B', 'D', 'E'],
    'D': ['B', 'C', 'E', 'F', 'G', 'H'],
    'E': ['C', 'D', 'F'],
    'F': ['E', 'D', 'G'],
    'G': ['A', 'F', 'D', 'H'],
    'H': ['G', 'D', 'A']
}

G1 = nx.from_dict_of_lists(ans_1)
# nx.draw_networkx(G, with_labels=True, node_color='Red', node_size=100)
# plt.show(block=True)
# node = nx.number_of_nodes(G)
# # print("number of nodes {}".format(node))
# edges = nx.number_of_edges(G)
# print("number of edges '{}' and node '{}'".format(edges, node))
# print("this the {} is connected {}".format(ans_1, nx.is_connected(G)))


route = pd.read_csv('air_routes.csv',  usecols=['source', 'dest', 'count'])
G = nx.from_pandas_edgelist(route, 'source', 'dest', edge_attr='count')
# nx.draw_networkx(G, with_labels=True, node_color='Green', node_size=10)
# plt.show(block=True)
print(" number of Airport '{}'".format(nx.number_of_nodes(G)))
print(" number of routes between two airport {}".format(nx.number_of_edges(G)))
short = nx.shortest_paths.all_shortest_paths(G, 'ALB', 'SFO')
print(nx.is_tree(G1))
print(nx.is_connected(G1))

