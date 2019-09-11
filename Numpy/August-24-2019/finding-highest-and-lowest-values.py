from __future__ import print_function
import numpy as np


h, l = np.loadtxt("data.csv", delimiter=",", usecols=(4, 5), unpack=True)

print("Highest: ", np.max(h))
print("Lowest: ", np.min(l))
print((np.max(h)+ np.min(l))/2)

print("Spread high price:", np.ptp(h))
print("Spread low price:", np.ptp(l))
