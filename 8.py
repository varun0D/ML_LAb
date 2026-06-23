# K-Means Clustering on Iris Dataset

from sklearn.datasets import load_iris
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
import pandas as pd

# Load Iris dataset
iris = load_iris()
X = iris.data

# Apply K-Means Clustering
kmeans = KMeans(n_clusters=3, random_state=42)
kmeans.fit(X)

# Cluster labels
labels = kmeans.labels_

# Create DataFrame
df = pd.DataFrame(X, columns=iris.feature_names)
df['Cluster'] = labels

# Print first few rows
print(df.head())

# Scatter Plot (using first two features)
plt.figure(figsize=(8, 6))
plt.scatter(X[:, 0], X[:, 1], c=labels, cmap='viridis', s=50)

# Plot cluster centroids
centroids = kmeans.cluster_centers_
plt.scatter(centroids[:, 0], centroids[:, 1],
            c='red', marker='X', s=200, label='Centroids')

plt.xlabel('Sepal Length')
plt.ylabel('Sepal Width')
plt.title('K-Means Clustering on Iris Dataset')
plt.legend()
plt.show()

# Display cluster centers
print("\nCluster Centers:")
print(centroids)
