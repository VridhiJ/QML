import numpy as np
import matplotlib.pyplot as plt

# Voltage range (simulate control knobs)
V1 = np.linspace(-1, 1, 100)
V2 = np.linspace(-1, 1, 100)
V1_grid, V2_grid = np.meshgrid(V1, V2)

# Define true "ideal" point where the quantum dot is stable
d1, d2 = 0.0, 0.0  # No drift yet

# Charge occupancy function (Gaussian bump centered at (d1, d2))
def charge_occupancy(V1, V2, d1, d2, a1=20, a2=20):
    return np.exp(-a1 * (V1 - d1)**2 - a2 * (V2 - d2)**2)

# Simulate initial state
Q = charge_occupancy(V1_grid, V2_grid, d1, d2)

# Plot the 2D charge diagram
plt.figure(figsize=(6, 5))
contour = plt.contourf(V1, V2, Q, levels=50, cmap='viridis')
plt.title("Quantum Dot Charge Stability Diagram (no drift)")
plt.xlabel("V1")
plt.ylabel("V2")
plt.colorbar(contour, label='Charge Occupancy')
plt.show()
