import networkx as nx
import matplotlib.pyplot as plt


# Graph A: Complete graph with 4 nodes
G_A = nx.complete_graph(4)

# Drawing function
def draw_graph(G, title):
    pos = nx.spring_layout(G, seed=42)
    plt.figure(figsize=(4, 4))
    nx.draw(G, pos, with_labels=True, node_color='lightgreen', edge_color='gray', node_size=600, font_size=14)
    plt.title(title)
    plt.show()

# Draw all graphs
draw_graph(G_A, "Graph A: 4-node complete graph")    