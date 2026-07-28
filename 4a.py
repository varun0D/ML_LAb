import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.datasets import load_iris

# Load Iris dataset
iris = load_iris()

# Create DataFrame
data = pd.DataFrame(iris.data, columns=iris.feature_names)

# Correlation Heatmap
sns.heatmap(data.corr(), annot=True)

plt.title("Iris Dataset Heatmap")
plt.show()
