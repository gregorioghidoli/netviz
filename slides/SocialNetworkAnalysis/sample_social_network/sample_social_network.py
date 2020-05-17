import networkx as nx
import matplotlib.pyplot as plt



G = nx.erdos_renyi_graph(7,0.5)

actors = {0:"Luca",1:"Edo",2:"Antonio",3:"Giacomo",
        4:"Joni",5:"Valeria",6:"Ennio"}

nx.draw_kamada_kawai(G,labels=actors,with_labels=True)
plt.savefig("sample_social.png")
plt.show()



