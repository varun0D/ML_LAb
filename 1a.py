import pandas as pd
import matplotlib.pyplot as plt
from sklearn.datasets import load_iris


iris = load_iris()


df = pd.DataFrame(iris.data, columns=iris.feature_names)
df['target'] = iris.target

pd.plotting.scatter_matrix(
    df.iloc[:, :-1],
    figsize=(10, 10),
    c=df['target'],
    marker='o',
    alpha=0.8
)

plt.suptitle("Scatter Plot Matrix for N-Dimensional Data")
plt.show()
