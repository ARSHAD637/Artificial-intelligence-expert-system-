import numpy as np

# Sigmoid activation
def sigmoid(x):
    return 1 / (1 + np.exp(-x))

# Derivative for backpropagation
def sigmoid_deriv(x):
    return x * (1 - x)

# XOR dataset
X = np.array([[0,0],[0,1],[1,0],[1,1]])
y = np.array([[0],[1],[1],[0]])

# Set seed and layer sizes
np.random.seed(42)
input_dim = 2
hidden_dim = 2
output_dim = 1

# Initialize weights/biases
W1 = np.random.randn(input_dim, hidden_dim)
b1 = np.zeros((1, hidden_dim))
W2 = np.random.randn(hidden_dim, output_dim)
b2 = np.zeros((1, output_dim))

# Training (Forward & Backward Propagation)
for epoch in range(10000):
    # Forward pass
    z1 = np.dot(X, W1) + b1
    a1 = sigmoid(z1)
    z2 = np.dot(a1, W2) + b2
    output = sigmoid(z2)
    
    # Loss (optional to print)
    # print(np.mean((y - output) ** 2))
    
    # Backpropagation
    error = y - output
    d_output = error * sigmoid_deriv(output)
    
    error_hidden = d_output.dot(W2.T)
    d_hidden = error_hidden * sigmoid_deriv(a1)
    
    # Update weights and biases
    W2 += a1.T.dot(d_output) * 0.1
    b2 += np.sum(d_output, axis=0, keepdims=True) * 0.1
    W1 += X.T.dot(d_hidden) * 0.1
    b1 += np.sum(d_hidden, axis=0, keepdims=True) * 0.1

# Test on the XOR input
print("Predicted Output:")
print(np.round(output))
