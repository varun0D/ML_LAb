import numpy as np
import matplotlib.pyplot as plt
from scipy.cluster.hierarchy import linkage, dendrogram

# Sample dataset
data = np.array([
    [1, 1],
    [1.5, 1.5],
    [5, 5],
    [6, 5],
    [3, 4]
])

# Single Linkage Clustering
single_link = linkage(data, method='single')

# Complete Linkage Clustering
complete_link = linkage(data, method='complete')

# Plot Dendrograms
plt.figure(figsize=(12, 5))

plt.subplot(1, 2, 1)
dendrogram(single_link)
plt.title("Agglomerative Clustering - Single Linkage")
plt.xlabel("Data Points")
plt.ylabel("Distance")

plt.subplot(1, 2, 2)
dendrogram(complete_link)
plt.title("Agglomerative Clustering - Complete Linkage")
plt.xlabel("Data Points")
plt.ylabel("Distance")

plt.tight_layout()
plt.show()
