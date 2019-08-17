# import libraries
import numpy as np # Import NumPy for data statistical analysis
import pandas as pd # Import Pandas for data manipulation using dataframes
import matplotlib.pyplot as plt # Import matplotlib for data visualisation
import seaborn as sns #Statistical data visualization

# Import Cancer data  from the Sklearn library
from sklearn.datasets import load_breast_cancer
cancer = load_breast_cancer()
df_cancer= pd.DataFrame(np.c_[cancer["data"],cancer["target"]],columns= np.append(cancer["feature_names"],["target"]))
df_cancer.head()

sns.pairplot(df_cancer, hue = 'target', vars = ['mean radius', 'mean texture', 'mean area', 'mean perimeter', 'mean smoothness'] )
plt.show()

sns.countplot(df_cancer["target"],label="Count")
plt.show()

sns.scatterplot(x="mean area", y="mean smoothness",hue="target",data=df_cancer)
plt.show()

#Strong correlation between the mean radius and mean perimeter, mean area and mean primeter
plt.figure(figsize=(20,10))
sns.heatmap(df_cancer.corr(),annot=True)

plt.show()