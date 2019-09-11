from __future__ import print_function
import numpy as np

c,v = np.loadtxt("data.csv",delimiter=",",usecols=(6,7),unpack=True)
vwap= np.average(c,weights=v)
print("VMAP=", vwap)