import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import splprep, splev

# Define the data points for the path
path_points = np.array([
    [1, 1], [3, 2], [5, 5], [6, 3], [8, 4]
])

# Separate x and y coordinates for the path points
x_path = path_points[:, 0]
y_path = path_points[:, 1]

# Fit a B-spline to the path points
tck, u = splprep([x_path, y_path], s=0)

# Evaluate the B-spline at 100 evenly spaced points
u_fine = np.linspace(0, 1, 100)
x_fine, y_fine = splev(u_fine, tck)

# Create plot
fig, ax = plt.subplots()

# Plot the original path points
ax.plot(x_path, y_path, 'go--', label='Original Path Points')

# Plot the B-spline fit
ax.plot(x_fine, y_fine, 'r-', label='B-spline Fit')

# Set limits and show plot
ax.set_xlim(0, 10)
ax.set_ylim(0, 7)
ax.legend()
plt.title('B-spline Fit with Stray Line Segment')
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.show()
