import networkx as nx
from networkx.algorithms import bipartite
import matplotlib.pyplot as plt

G = nx.Graph()
G.add_nodes_from(["Edoardo","Gianluca","Lorenzo","Cristian"],bipartite=0)
G.add_nodes_from(["Alice","Anna","Claudia","Sara"],bipartite=1)

G.add_edges_from([("Alice","Edoardo"),("Anna","Lorenzo"),("Anna","Edoardo"),
                 ("Claudia","Gianluca"),("Claudia","Lorenzo"),("Gianluca","Alice"),
                 ("Sara","Cristian"),("Sara","Lorenzo")])

male, female = bipartite.sets(G)
pos = dict()
pos.update( (n, (1, i)) for i, n in enumerate(male) ) 
pos.update( (n, (2, i)) for i, n in enumerate(female) ) 

nx.draw(G,with_labels=True, pos=pos)
plt.savefig("sample_two-mode_network.png")
plt.show()




