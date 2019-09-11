import numpy as np

c,v = np.loadtxt("data.csv",delimiter= ",", usecols=(3,7),unpack=True)
vwap = np.average(c,weights =v)
print("VMAP: " , vwap)

print("Mean: ", np.mean(c))

t = np.arange(len(c))
print("TWAP: ", np.average(c,weights=t))