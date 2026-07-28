import pandas as pd
import matplotlib.pyplot as plt
from sklearn.datasets import load_iris

iris = load_iris()
data = pd.DataFrame(iris.data, columns=iris.feature_names)

ax = plt.axes(projection='3d')

ax.plot_trisurf(
    data['sepal length (cm)'],
    data['sepal width (cm)'],
    data['petal length (cm)'],
    cmap='viridis'
)

ax.set_xlabel('Sepal Length')
ax.set_ylabel('Sepal Width')
ax.set_zlabel('Petal Length')

plt.show()
