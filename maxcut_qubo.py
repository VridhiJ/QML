import networkx as nx
import matplotlib.pyplot as plt


from qiskit_optimization.applications import Maxcut
from qiskit.circuit.library import QAOAAnsatz

from qiskit.primitives import Estimator
from scipy.optimize import minimize
import numpy as np

import json
from pathlib import Path

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

# Hamiltonian representation
qubit_op, offset = qp.to_ising()

# View the Hamiltonian
print("Cost function Hamiltonian in Pauli form:")
print(qubit_op)

# -------------------------------
# STEP 3: Setup QAOA
# -------------------------------

circuit = QAOAAnsatz(cost_operator=qubit_op, reps=2)

# For drawing, so that estimator doesn't crash due to measurements
# since we are feeding circuit into unitary-only backend
circuit_with_measure = circuit.copy()
circuit_with_measure.measure_all()

# Draw circuit, with measurement
circuit_with_measure.draw('mpl')
plt.show()

# -------------------------------
# STEP 4: Cost Function Estimator
# -------------------------------

estimator = Estimator()
objective_func_vals = []  # store cost per iteration

def cost_func_estimator(params):
    job = estimator.run([circuit], [qubit_op], [params])
    result = job.result()
    cost = result.values[0]
    objective_func_vals.append(cost)
    return cost

# For 2 reps: [γ₁, β₁, γ₂, β₂]
initial_gamma = np.pi
initial_beta = np.pi/2
init_params = [initial_gamma, initial_beta, initial_gamma, initial_beta]

result = minimize(
    cost_func_estimator,
    x0=init_params,
    method='COBYLA',
    tol=1e-2
)

# -------------------------------
# STEP 5: Plot QAOA convergence
# -------------------------------

print("Final cost:", result.fun)
print("Optimal parameters:", result.x)

plt.plot(objective_func_vals, marker='o')
plt.xlabel("Iteration")
plt.ylabel("Cost ⟨H⟩")
plt.title("QAOA Convergence on Graph A")
plt.grid(True)
plt.show()



# -------------------------------
# STEP 6: Save Output for Transfer
# -------------------------------

Path("results").mkdir(exist_ok=True)

with open("results/graph_a_params.json", "w") as f:
    json.dump({
        "optimal_params": result.x.tolist(),
        "final_cost": result.fun,
        "cost_trajectory": objective_func_vals
    }, f)

