import matplotlib.pyplot as plt
import seaborn as sns

titanic_data = sns.load_dataset("titanic")
titanic_data.head()

sns.countplot(x="class", data=titanic_data)
plt.show()

sns.countplot(x="survived", data=titanic_data)
plt.show()

sns.boxplot(x="class", y="age",data=titanic_data)
plt.show()

sns.swarmplot(x="class", y="age", data=titanic_data)
plt.show()

sns.jointplot(x="fare", y="age", data=titanic_data)
plt.show()

sns.distplot(titanic_data["fare"], bins=25, kde=False, color="blue")
plt.show()

plt.figure(figsize=(10,10))
sns.heatmap(titanic_data.corr(),annot=True)
plt.show()