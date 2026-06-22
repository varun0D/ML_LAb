import matplotlib.pyplot as plt
from sklearn.datasets import load_iris
from scipy.cluster.hierarchy import linkage, dendrogram

# Load Iris dataset
iris = load_iris()
X = iris.data

# Perform Agglomerative Clustering
single_linkage = linkage(X, method='single')
complete_linkage = linkage(X, method='complete')

# Plot dendrograms
plt.figure(figsize=(14, 6))

# Single Linkage Dendrogram
plt.subplot(1, 2, 1)
dendrogram(single_linkage)
plt.title("Iris Dataset - Single Linkage")
plt.xlabel("Samples")
plt.ylabel("Euclidean Distance")

# Complete Linkage Dendrogram
plt.subplot(1, 2, 2)
dendrogram(complete_linkage)
plt.title("Iris Dataset - Complete Linkage")
plt.xlabel("Samples")
plt.ylabel("Euclidean Distance")

plt.tight_layout()
plt.show()
