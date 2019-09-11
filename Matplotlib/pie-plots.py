import matplotlib.pyplot as plt

plt.rcdefaults()

values = [20,55,5,17,3]
colors = ["g","r","y","b","m"]
explode = [0,0.5,0,0,0.5]
labels = ["Egypt","United States","Canada","China","Europe"]
plt.pie(values,colors=colors, labels=labels, explode= explode)
plt.title("Countries")
plt.show()