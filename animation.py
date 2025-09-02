import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib.animation import FuncAnimation
fig, ax = plt.subplots(figsize=(8.5, 8.5))
ax.set_xlim(70, 330)
ax.set_ylim(30, 350)
ax.set_aspect('equal')
ax.axis('off')
fig.patch.set_facecolor('#090909')  # Background color
ax.set_facecolor('#090909')
# Number of points
NUM_POINTS = 12000
# Initialize scatter plot with dummy data
scatter = ax.scatter([], [], c=[], s=[], cmap='plasma', edgecolors='none', alpha=0.85)
def generate_points(t):
    """Generate points and features for a given time t"""
    i = np.arange(NUM_POINTS, -1, -1)
    x = i
    y = i / 235.0
    k = (4 + np.sin(x / 11 + 8 * t)) * np.cos(x / 14)
    e = y / 8 - 19
    d = np.sqrt(k ** 2 + e ** 2) + np.sin(y / 9 + 2 * t)
    q = 2 * np.sin(2 * k) + np.sin(y / 17) * k * (9 + 2 * np.sin(y - 3 * d))
    c = d ** 2 / 49 - t
    xp = q + 50 * np.cos(c) + 200
    yp = q * np.sin(c) + d * 39 - 440
    yp = 400 - yp  # Flip vertically
    # Color mapped to d (distance) or c
    colors = d
    sizes = 0.5 + 2.5 * np.abs(np.sin(c))  # Slight size animation
    return np.column_stack((xp, yp)), colors, sizes
def update(frame):
    """Update function for animation"""
    t = frame * 2 * np.pi / 45 # much faster
    coords, colors, sizes = generate_points(t)
    scatter.set_offsets(coords)
    scatter.set_array(colors)      # Update color
    scatter.set_sizes(sizes)       # Update size
    return scatter,
# Create animation
anim = FuncAnimation(fig, update, frames=150, interval=50, blit=True, repeat=True)
# Show the animation
plt.tight_layout()
plt.show()