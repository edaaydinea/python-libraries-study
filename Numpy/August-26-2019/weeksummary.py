from __future__ import print_function
import numpy as np
from datetime import datetime

"""
Monday 0
Tuesday 1
Wednesday 2
Thursday 3
Friday 4
Saturday 5
Sunday 6
"""


def datestr2num(s):
    return datetime.strptime(s, "%d-%m-%Y").date().weekday()


dates, open, high, low, close = np.loadtxt("data.csv", delimiter=",", usecols=(1, 2, 3, 4, 5),
                                           converters={1: datestr2num}, unpack=True)
close = close[:16]
dates = dates[:16]

# get first Monday
# o dedik çünkü sıralama bu şekilde gidiyor. 0 dedik çünkü en baştaki değere bakacağız.
first_monday = np.ravel(np.where(dates == 0))[0]
print("The first Monday index is ", first_monday)

# get last Friday
# 4 dedik çünkü sıralama bu şekilde gidiyor. -1 dedik çünkü en sonki değere bakacağız.
last_friday = np.ravel(np.where(dates == 4))[-1]
print("The last Friday index is ", last_friday)

# Tüm hafta bilgileri burada olacak. tek biraray şeklinde.
week_indices = np.arange(first_monday, last_friday + 1)
print("Weeks indices initial: ", week_indices)

# yukarıdaki array'i 3 array olacak şekilde parçalayacağız. 3 burada axis oluyor.
# 3 tane axis, satır olacak diyoruz.
week_indices = np.split(week_indices, 3)
print("Weeks indices after split", week_indices)


def summarize(array, open, high, low, close):
    monday_open = open[array[0]]
    week_high = np.max(np.take(high, array))
    week_low = np.min(np.take(low, array))
    friday_close = close[array[-1]]

    return "APPL", monday_open, week_high, week_low, friday_close


weeksummary = np.apply_along_axis(summarize, 1, week_indices, open, high, low, close)
print("Week summary", weeksummary)

np.savetxt("weeksummary.csv",weeksummary,delimiter=",", fmt="%s")


"""
The first Monday index is 1
The last Friday index is 15
Week indices after split [array([1,2,3,4,5]),array([6,7,8,9,10]),array([11,12,13,14,15])]

Week summary [['APPL' '335.8' '346.7' '334.3' '346.5'] 
['APPL' '347.89' '360.0' '347.64' '356.85'] 
['APPL' '356.79' '364.9' '349.52' '350.56']]

"""