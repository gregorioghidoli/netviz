import networkx as nx
import matplotlib.pyplot as plt

G = nx.Graph()
G.add_nodes_from(['a','b','c','d','e','f','g'])

nx.draw(G,with_labels=True,label="empty graph")
plt.savefig("empty_graph.png")
plt.show()

G.add_edges_from(
    [("a","c"),("f","d"), ("d","c"),("b","d"),
     ("c","e"),("a","g"),("g","e")])


nx.draw_kamada_kawai(G,with_labels=True,label="sparse graph")
plt.savefig("sparse_graph.png")
plt.show()

G.add_edges_from([("c","g"),("f","a"),("g","d"),("d","e"),
                  ("b","c"),("g","b"),("a","b")])

nx.draw_kamada_kawai(G,with_labels=True,label="dense graph")
plt.savefig("dense_graph.png")
plt.show()

G.add_edges_from([("g","f"),("e","f"),("c","f"),("e","b"),
                  ("a","d"),("e","a"),("b","f")])

nx.draw_kamada_kawai(G,with_labels=True,label="clique")
plt.savefig("complete_graph.png")
plt.show()


