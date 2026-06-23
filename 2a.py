import pandas as pd
import matplotlib.pyplot as plt

# Load dataset
dataset = pd.read_csv('./ToyotaCorolla.csv')

# Select columns
x = dataset['KM']
y = dataset['Doors']
z = dataset['Price']

# Create 3D plot
ax = plt.axes(projection='3d')
ax.plot_trisurf(x, y, z, cmap='jet')

ax.set_xlabel('KM')
ax.set_ylabel('Doors')
ax.set_zlabel('Price')
ax.set_title('3D Surface Plot')

plt.show()
