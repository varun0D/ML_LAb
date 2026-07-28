import matplotlib.pyplot as plt
from sklearn.datasets import load_iris

iris = load_iris()

plt.boxplot(iris.data)
plt.title("Iris Box Plot")
plt.show()
