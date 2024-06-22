import matplotlib.pyplot as plt
import numpy as np

# Generating data points
num_points = 20
x = np.arange(1, num_points + 1)
y1 = np.random.randint(5, 15, num_points)  # Oxygen levels
y2 = np.random.randint(70, 120, num_points)  # Blood pressure

# Plotting the data
plt.plot(x, y1, marker='o', linestyle='-', color='blue', label='Zuurstof')
plt.plot(x, y2, marker='s', linestyle='--', color='red', label='Bloeddruk')

# Adding labels and title
plt.xlabel('Tijd')
plt.ylabel('Waarde')
plt.title('Zuurstof en bloeddruk (Matplotlib)')

# Adding grid
plt.grid(True)

# Adding legend
plt.legend()

# Adding annotations
for i in range(num_points):
    plt.text(x[i], y1[i], f"{y1[i]}", ha='right', va='bottom')
    plt.text(x[i], y2[i], f"{y2[i]}", ha='right', va='bottom')

# Show plot
plt.tight_layout()
plt.show()
