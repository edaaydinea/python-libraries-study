import numpy as np

"""
-- The array m has 24 elements with values 0 to 23 and we reshaped it to be a 
two-by-three-by-four, three dimensional array.
-- We can visualize this as two-story building w,th 12 rooms on each floor,
3 rows and 4 columns(alternatively we can think of it as a spreadsheet
with sheets,rows and columns).
--
"""

m = np.arange(24).reshape(2,3,4)
print(m.shape)
print("1-------")
print(m)
print("2-------")
"""
We can select a single room using its three coordinates, namely, the floor,
column and row. For example, the room on the first floor, in the first row.
For example, the room on the first floor, in the first column ( we can 
have floor 0 and room 0 - it's just a matter of convention) can be 
represented by the following:
"""

print(m[0,0,0])
print("3-------")
"""
If we don't care about the floor, but still want the first column and row,
we replace the first index by a: (colon) beacuse we just need to specify the
floor number and omit the other indices:
"""

print(m[:,0,0])
print("4-------")
# We can also write this:

print(m[0,:,:])
print("5-------")

# We can also write this:

print(m[0,...])
print("6-------")

# Using steps to slice
"""
First number represents to matrix number, second number represent row number,
third number represents to column number. 1::2 represents to from zeroth
element to second number.
"""
print(m[1,1,::2])
print("7-------")

# Using an ellipsis to slice
"""
If we want to select all the rooms on the both floors that are in the second
column, regardless of the row. 
"""

print(m[...,1])
print("8-------")

"""
Similarly, select all the rooms on the second row, regardless of floor and
column, by writing the following code snippet: 
"""

print(m[:,1])
print("9-------")

"""
If we want to select rooms on the ground floor second column
"""

print(m[0,:,1])
print("10-------")


# Using negative indices

"""
If we want to select the first floor, last column, then type the following
code snippet
"""

print(m[0,:,-1])
print("11-------")

"""
If we want to select rooms on the ground floor, last column reserved, the type
the following code snippet
"""

print(m[0,::-1,-1])
print("12-------")

"""
Select every second element of that slice as follows:
"""

print(m[0,::2,-1])
print("13-------")

"""
The command that reserves a one-dimensional array puts the top floor following 
the ground floor as follows: 
"""

print(m[::-1])
print("14-------")

