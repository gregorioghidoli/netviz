import networkx as nx
import matplotlib.pyplot as plt

G = nx.Graph()

G.add_nodes_from(["a","b","c","d","e"])

G.add_edges_from([("a","c"),("a","d"),("b","d"),
                  ("c","d"),("c","e"),("d","e")])

nx.draw_kamada_kawai(G,with_labels=True)
plt.savefig("sample_graph.png")
plt.show()
