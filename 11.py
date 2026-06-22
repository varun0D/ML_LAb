import numpy as np

# Activation Function (Step Function)
def activation(x):
    return 1 if x >= 0 else 0

# Perceptron Training Function
def train_perceptron(inputs, targets, learning_rate=0.1, epochs=10):
    weights = np.zeros(inputs.shape[1])
    bias = 0

    for _ in range(epochs):
        for x, target in zip(inputs, targets):
            net_input = np.dot(x, weights) + bias
            output = activation(net_input)

            error = target - output

            weights += learning_rate * error * x
            bias += learning_rate * error

    return weights, bias

# Perceptron Testing Function
def test_perceptron(inputs, weights, bias):
    print("Input\tOutput")
    for x in inputs:
        net_input = np.dot(x, weights) + bias
        output = activation(net_input)
        print(f"{x}\t{output}")

# Input Data
X = np.array([
    [0, 0],
    [0, 1],
    [1, 0],
    [1, 1]
])

# AND Function
print("Training Perceptron for AND Function")
AND_targets = np.array([0, 0, 0, 1])
weights_and, bias_and = train_perceptron(X, AND_targets)

print("\nTesting AND Function")
test_perceptron(X, weights_and, bias_and)

# OR Function
print("\nTraining Perceptron for OR Function")
OR_targets = np.array([0, 1, 1, 1])
weights_or, bias_or = train_perceptron(X, OR_targets)

print("\nTesting OR Function")
test_perceptron(X, weights_or, bias_or)
