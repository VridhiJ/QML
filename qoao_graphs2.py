import networkx as nx
import matplotlib.pyplot as plt

from qiskit import Aer
from qiskit.utils import algorithm_globals, QuantumInstance
from qiskit_optimization.applications.ising import max_cut
from qiskit_optimization.converters import QuadraticProgramToQubo
from qiskit_optimization.problems import QuadraticProgram
from qiskit.algorithms.minimum_eigensolvers import QAOA
from qiskit.algorithms import MinimumEigenOptimizer
from qiskit.circuit.library import TwoLocal

# -------------------------------
# STEP 1: Build and Visualize Graph A (Complete Graph)
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
qubit_op, offset = max_cut.get_operator(w)

# Optional: View the Hamiltonian
print("Cost Hamiltonian (Pauli form):")
print(qubit_op)

# -------------------------------
# STEP 3: Setup QAOA
# -------------------------------
algorithm_globals.random_seed = 42
backend = Aer.get_backend('aer_simulator_statevector')

qaoa = QAOA(reps=1, quantum_instance=QuantumInstance(backend, seed_simulator=42, seed_transpiler=42))
optimizer = MinimumEigenOptimizer(qaoa)

# -------------------------------
# STEP 4: Solve the MaxCut Problem
# -------------------------------
qp = max_cut.get_quadratic_program(w)
result = optimizer.solve(qp)

print("\n🧠 QAOA Solution:")
print("Bitstring:", result.x)
print("MaxCut value:", result.fval)
