import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Curve25519 parameters
A = 486662

# Create meshgrid
x = np.linspace(-100, 100, 400)
y = np.linspace(-100, 100, 400)
X, Y = np.meshgrid(x, y)

# Compute Z = Y^2 - (X^3 + A*X^2 + X)
Z = Y**2 - (X**3 + A*X**2 + X)

# Plot
fig = plt.figure(figsize=(12, 8))
ax = fig.add_subplot(111, projection='3d')
ax.plot_surface(X, Y, Z, cmap='coolwarm', edgecolor='none', alpha=0.9)

ax.set_title("Curve25519 in 3D: y² = x³ + 486662x² + x", fontsize=14)
ax.set_xlabel("x")
ax.set_ylabel("y")
ax.set_zlabel("y² - (x³ + Ax² + x)")
plt.tight_layout()
plt.show()
