import numpy as np
import matplotlib.pyplot as plt

# Given data points
x = [1, 2, 3, 4, 5, 6]
y = [5.5, 43.1, 128, 290.7, 498.4, 978.67]

# Fit a 4th-degree polynomial to the data
p = np.polyfit(x, y, 4)

# Generate x values for the polynomial curve
x2 = np.arange(1, 6.1, 0.1)

# Compute the y values of the polynomial curve
y2 = np.polyval(p, x2)

# Plot the original data points and the polynomial curve
plt.plot(x, y, 'o', label='Original Data')
plt.plot(x2, y2, label='4th Degree Polynomial Fit')
plt.xlabel('x')
plt.ylabel('y')
plt.title('Polynomial Fit')
plt.legend()
plt.grid(True)
plt.show()