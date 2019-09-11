import numpy as np
import matplotlib.pyplot as plt
import random

# Figure
# Determine the figure size
fig = plt.figure(figsize=(14,14))

# Create random number
X = np.random.randn(600)
Y = np.random.randn(600)

plt.scatter(X,Y)

plt.show()