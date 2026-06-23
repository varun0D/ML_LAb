import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load dataset
data = pd.read_csv("./ToyotaCorolla.csv")

# Correlation heatmap
sns.heatmap(
    data[["Price", "KM", "Doors", "Weight"]].corr(),
    cmap="jet",
    annot=True
)

plt.title("Heatmap of Toyota Corolla Dataset")
plt.show()
