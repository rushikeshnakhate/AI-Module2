import warnings
import pandas as pd
import networkx as nx  # "nx" is a conventional alias for "networkx" when importing
import matplotlib.pyplot as plt

warnings.filterwarnings("ignore")  # To suppress matplotlib warning messages

# Build a dataframe with 4 connections
graph_str_labels = {
    'A': ['B', 'E'],
    'B': ['A', 'C', 'E'],
    'C': ['B', 'D'],
    'D': ['C', 'E', 'F'],
    'E': ['A', 'B', 'D'],
    'F': ['D']
}
# Build your graph
G = nx.from_dict_of_lists(graph_str_labels)
print(type(G))
nx.draw_networkx(G, with_labels=True, node_color='cyan', node_size=500)

df = pd.read_csv("facebook_combined.txt", sep=' ', usecols=['A', 'B'], nrows=10)
# construct graph from pandas
G = nx.from_pandas_edgelist(df, 'A', 'B')
nx.draw_networkx(G)
plt.show(block=True)

G = nx.graph
