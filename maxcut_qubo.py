import networkx as nx
import matplotlib.pyplot as plt
# -------------------------------
# STEP 1: Build and Visualize Graph A
# -------------------------------
G = nx.complete_graph(4)
pos = nx.spring_layout(G, seed=42)

plt.figure(figsize=(4, 4))
nx.draw(G, pos, with_labels=True, node_color='lightblue', node_size=600, edge_color='gray')
plt.title("Graph A: Complete 4-Node")
plt.show()