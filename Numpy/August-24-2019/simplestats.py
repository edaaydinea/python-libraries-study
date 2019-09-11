import numpy as np

c = np.loadtxt("data.csv", delimiter=",",usecols=(6,),unpack= True)

print("Median:", np.median(c))

sorted_close = np.msort(c)
print("Sorted: ", sorted_close)