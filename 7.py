# KNN Classifier using Euclidean and Manhattan Distance
# Glass Dataset

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix

# Load Glass Dataset
# Replace 'glass.csv' with your dataset path
data = pd.read_csv("glass.csv")

# Features and Target
X = data.iloc[:, :-1]   # all columns except class
y = data.iloc[:, -1]    # class column

# Split dataset into 70% training and 30% testing
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.30, random_state=42
)

# -------------------------------
# KNN with Euclidean Distance
# -------------------------------
knn_euclidean = KNeighborsClassifier(
    n_neighbors=3,
    metric='euclidean'
)

knn_euclidean.fit(X_train, y_train)
y_pred_euclidean = knn_euclidean.predict(X_test)

print("===== KNN using Euclidean Distance (k=3) =====")
print("Accuracy:", accuracy_score(y_test, y_pred_euclidean))
print("\nConfusion Matrix:")
print(confusion_matrix(y_test, y_pred_euclidean))
print("\nClassification Report:")
print(classification_report(y_test, y_pred_euclidean))

# -------------------------------
# KNN with Manhattan Distance
# -------------------------------
knn_manhattan = KNeighborsClassifier(
    n_neighbors=3,
    metric='manhattan'
)

knn_manhattan.fit(X_train, y_train)
y_pred_manhattan = knn_manhattan.predict(X_test)

print("\n===== KNN using Manhattan Distance (k=3) =====")
print("Accuracy:", accuracy_score(y_test, y_pred_manhattan))
print("\nConfusion Matrix:")
print(confusion_matrix(y_test, y_pred_manhattan))
print("\nClassification Report:")
print(classification_report(y_test, y_pred_manhattan))
