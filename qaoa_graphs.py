import networkx as nx
import matplotlib.pyplot as plt


# Graph A: Complete graph with 4 nodes
G_A = nx.complete_graph(4)

# Graph B: Graph A minus one edge
G_B = G_A.copy()
G_B.remove_edge(0, 1)

# Graph C: 5-node cycle with one added chord
G_C = nx.cycle_graph(5)
G_C.add_edge(0, 2)  # add a chord

# Drawing function
def draw_graph(G, title):
    pos = nx.spring_layout(G, seed=42)
    plt.figure(figsize=(4, 4))
    nx.draw(G, pos, with_labels=True, node_color='lightgreen', edge_color='gray', node_size=600, font_size=14)
    plt.title(title)
    plt.show()

# Draw all graphs
draw_graph(G_A, "Graph A: 4-node complete graph")    
draw_graph(G_B, "Graph B:  graph missing edge 0–1")
draw_graph(G_C, "Graph C: 5-node Circle + Chord")