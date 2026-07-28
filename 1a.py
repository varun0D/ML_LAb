import pandas as pd
import matplotlib.pyplot as plt
from sklearn.datasets import load_iris

# Load Iris dataset
iris = load_iris()

# Create DataFrame
df = pd.DataFrame(iris.data, columns=iris.feature_names)

# Scatter plot matrix
pd.plotting.scatter_matrix(
    df,
    figsize=(10, 10),
    marker='o',
    alpha=0.8
)

plt.suptitle("Scatter Plot Matrix for N-Dimensional Data")
plt.show()
