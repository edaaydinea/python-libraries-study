import numpy as np

t= np.dtype( [ ('name', np.str_, 40), ('numitems', np.int32),('price',np.float32)])
print(t)