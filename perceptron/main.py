import numpy as np

class Perceptron:
    def __init__(self, num_inputs):
        self.weights = np.zeros(num_inputs)
        self.bias = 0

    def predict(self, inputs):
        weighted_sum = np.dot(inputs, self.weights) + self.bias
        activation = 0 if weighted_sum <= 0 else 1
        return activation

    def train(self, training_inputs, labels, learning_rate, num_epochs):
        for _ in range(num_epochs):
            for inputs, label in zip(training_inputs, labels):
                prediction = self.predict(inputs)
                update = learning_rate * (label - prediction)
                self.weights += update * inputs
                self.bias += update


training_inputs = np.array([[0, 0], [0, 1], [1, 0], [1, 1]])
labels = np.array([0, 0, 0, 1])

perceptron = Perceptron(num_inputs=2)
perceptron.train(training_inputs, labels, learning_rate=0.1, num_epochs=10)

test_inputs = np.array([[0, 0], [0, 1], [1, 0], [1, 1]])
for inputs in test_inputs:
    prediction = perceptron.predict(inputs)
    print(f"Input: {inputs}  Prediction: {prediction}")