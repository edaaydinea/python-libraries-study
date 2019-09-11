import numpy as np

print("HORIZONTAL SPLITTING \n")

a = np.arange(9,).reshape(3,3)
print(a)

a_hsplit= np.hsplit(a,3)
print(a_hsplit)

a_split= np.split(a,3,axis=1)
print(a_split)


print("\nVERTICAL SPLITTING \n")

b= np.arange(9).reshape(3,3)
b_vsplit= np.vsplit(a,3)
print(b_vsplit)

b_split= np.split(a,3,axis=0)
print(b_split)

print("\nDEPTH-WISE SPLITTING \n")

c = np.arange(27).reshape(3,3,3)
print(c)

c_dsplit= np.dsplit(c,3)
print(c_dsplit)

