import numpy as np

b= np.arange(24).reshape(2,12)
print(b)

# The ndim attribute gives the number of dimensions.
print(b.ndim)

# The size attribute contains the number of elements.
print(b.size)

# The itemsize attribute gives the number of bytes for each element in the array:
print(b.itemsize)

#