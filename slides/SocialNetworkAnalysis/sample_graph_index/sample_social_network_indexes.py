import networkx as nx
import matplotlib.pyplot as plt

actors = ["Ann","Bart","Holly","Homer","John",
          "Phil","George","Lisa","Marge","Michael"]

ties = [("Bart","Ann"),("Ann","Holly"),("Ann","George"),
        ("Bart","Holly"),("Bart","Homer"),("Bart","George"),
        ("Holly","Homer"),("Holly","John"),("Holly","Phil"),
        ("Holly","George"),("Homer","John"),("Homer","Phil"),
        ("John","Phil"),("George","Phil"),("Phil","Lisa"),
        ("George","Lisa"),("Lisa","Marge"),("Marge","Michael")]

G = nx.Graph()

G.add_nodes_from(actors)
G.add_edges_from(ties)

cci = nx.closeness_centrality(G)

cbi = nx.betweenness_centrality(G)

print(str(nx.density(G)) + '\n')
print(str(nx.degree(G)) + '\n')
print(str(cci) + '\n')
print(str(cbi) + '\n')
print(str(max(nx.degree(G))) + '\n' )
print(str(max(cci,key=cci.get)) + '\n')
print(str(max(cci,key=cci.get)) + '\n')

nx.draw_kamada_kawai(G,with_labels=True)
plt.savefig("sample_social.png")
plt.show()

chosen_nodes = ['Ann','George','Phil','Lisa']
nx.draw_kamada_kawai(nx.subgraph(G,chosen_nodes),with_labels=True)
plt.savefig("sample_subgraph.png")
plt.show()

Cl = list(nx.find_cliques(G))
maxcl = []

for l in Cl:
    if len(l) > len(maxcl):
        maxcl = l
    
clique = nx.complete_graph(len(maxcl))
clique_nodes = { i : maxcl[i] for i in range(0, len(maxcl) ) }
nx.draw_kamada_kawai(clique,labels=clique_nodes,with_labels=True)
plt.savefig("sample_clique.png")
plt.show()


