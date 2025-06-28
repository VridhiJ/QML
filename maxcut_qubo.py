import networkx as nx
import matplotlib.pyplot as plt

from qiskit_optimization.applications import Maxcut

# -------------------------------
# STEP 1: Build and Visualize Graph A
# -------------------------------
G = nx.complete_graph(4)
pos = nx.spring_layout(G, seed=42)

plt.figure(figsize=(4, 4))
nx.draw(G, pos, with_labels=True, node_color='lightblue', node_size=600, edge_color='gray')
plt.title("Graph A: Complete 4-Node")
plt.show()

# -------------------------------
# STEP 2: Convert Graph to MaxCut QUBO
# -------------------------------
w = nx.adjacency_matrix(G).todense()
max_cut = Maxcut(w)
qp = max_cut.to_quadratic_program()
print(qp.prettyprint())
#qubit_op, offset = max_cut.get_operator(w)

# View the Hamiltonian
#print("Cost Hamiltonian in Pauli form:")
#print(qubit_op)