# PCA and LDA Implementation using Scikit-Learn

import numpy as np
from sklearn.datasets import load_iris
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis
import matplotlib.pyplot as plt

# Load dataset
iris = load_iris()
X = iris.data
y = iris.target

# Standardize the data
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# ---------------- PCA ----------------
pca = PCA(n_components=2)
X_pca = pca.fit_transform(X_scaled)

print("PCA Explained Variance Ratio:")
print(pca.explained_variance_ratio_)

# ---------------- LDA ----------------
lda = LinearDiscriminantAnalysis(n_components=2)
X_lda = lda.fit_transform(X_scaled, y)

# ---------------- Visualization ----------------
plt.figure(figsize=(12,5))

# PCA Plot
plt.subplot(1,2,1)
for target in np.unique(y):
    plt.scatter(
        X_pca[y == target, 0],
        X_pca[y == target, 1],
        label=iris.target_names[target]
    )
plt.title("PCA")
plt.xlabel("Principal Component 1")
plt.ylabel("Principal Component 2")
plt.legend()

# LDA Plot
plt.subplot(1,2,2)
for target in np.unique(y):
    plt.scatter(
        X_lda[y == target, 0],
        X_lda[y == target, 1],
        label=iris.target_names[target]
    )
plt.title("LDA")
plt.xlabel("Linear Discriminant 1")
plt.ylabel("Linear Discriminant 2")
plt.legend()

plt.tight_layout()
plt.show()
