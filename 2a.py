import pandas as pd
import matplotlib.pyplot as plt
from sklearn.datasets import load_iris

# Load Iris dataset
iris = load_iris()
data = pd.DataFrame(iris.data, columns=iris.feature_names)

# Select columns
x = data['sepal length (cm)']
y = data['sepal width (cm)']
z = data['petal length (cm)']

# Create 3D Surface Plot
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

ax.plot_trisurf(x, y, z, cmap='viridis')

# Labels
ax.set_xlabel('Sepal Length')
ax.set_ylabel('Sepal Width')
ax.set_zlabel('Petal Length')
ax.set_title('3D Surface Plot of Iris Dataset')

plt.show()
