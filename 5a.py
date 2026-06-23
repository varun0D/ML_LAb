import pandas as pd
import matplotlib.pyplot as plt
from sklearn.datasets import load_iris

# Load Iris dataset
iris = load_iris()

# Create DataFrame
df = pd.DataFrame(iris.data, columns=iris.feature_names)

# Display first few records
print(df.head())

# Box Plot
plt.figure(figsize=(10, 6))
df.boxplot()
plt.title("Box Plot of Iris Dataset Features")
plt.ylabel("Values")
plt.xticks(rotation=45)
plt.grid(True)
plt.show()
