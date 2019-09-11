import numpy as np

b = np.array([1. + 1j, 3 + 2.j])
print(b)

"""
Convert a NumPy array to a Python list with tolist() function
"""

print(b.tolist())

"""
The astype() function converts the array to an array of the specified type
"""

print(b.astype(int))

""""
We are losing the imaginary part when casting from the NumPy complex type ( not the plain
vanilla Python one) to int. The astype() function also accepts the name of a type a string. 
"""

print(b.astype("complex"))