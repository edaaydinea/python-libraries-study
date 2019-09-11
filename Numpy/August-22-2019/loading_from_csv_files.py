import numpy as np
import csv

c,v = np.loadtxt("data.csv", delimiter=",", usecols=(6, 7), unpack=True)