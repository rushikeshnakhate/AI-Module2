import networkx as nx
import matplotlib.pyplot as plt

File = 'SiouxFalls_flow.txt'
G3 = nx.DiGraph()
with open(File, "r") as f:
    line = f.readline()
    line = f.readline()
    while len(line):
        l = line.split()
        fromnode = int(l[0])
        to = int(l[1])
        volume = float(l[2])
        cost = float(l[3])
        G3.add_edge(fromnode, to, weight=cost)
        line = f.readline()

# create Plot of Netweork
plt.figure(figsize=(8, 12))
node_pos = nx.get_node_attributes(G3, 'pos')
arc_weight = nx.get_edge_attributes(G3, 'weight')
sp = nx.dijkstra_path(G3, source=1, target=20)

red_edges = list(zip(sp, sp[1:]))
node_col = ['white' if not node in sp else 'red' for node in G3.node()]
egde_col = ['black' if not edge in red_edges else 'red' for edge in G3.edges()]
nx.draw_networkx(G3, node_pos, node_color=node_col, node_size=450)
plt.show(block=True)
