import matplotlib.pyplot as plt
from sklearn.datasets import load_iris

# Load Iris dataset
iris = load_iris()

# Select columns
x = iris.data[:, 0]   # Sepal Length
y = iris.data[:, 1]   # Sepal Width
z = iris.data[:, 2]   # Petal Length

# Contour plot
plt.tricontourf(x, y, z)
plt.colorbar()

plt.xlabel("Sepal Length")
plt.ylabel("Sepal Width")
plt.title("Contour Plot (Iris Dataset)")

plt.show()
