import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Load Toyota dataset
dataset = pd.read_csv('./ToyotaCorolla.csv')

# Select variables
x = dataset['KM']
y = dataset['Weight']
z = dataset['Price']

# Create contour plot
plt.tricontourf(x, y, z, levels=20, cmap='jet')
plt.colorbar(label='Price')

plt.xlabel('KM')
plt.ylabel('Weight')
plt.title('Contour Plot')

plt.show()
