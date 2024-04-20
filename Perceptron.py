import numpy as np

class Perceptron:
    def __init__(self, name, num_inputs):
        self.name = name
        self.weights = np.random.rand(num_inputs)
        self.bias = np.random.rand()

    def predict(self, image):
        # Flatten the image matrix into a 1D array
        flattened_image = image.flatten()
        
        # Compute the weighted sum
        weighted_sum = np.dot(flattened_image, self.weights) + self.bias
        
        # Apply activation function (Step function)
        return 1 if weighted_sum > 0 else 0

    def train(self, positive_examples, num_epochs, learning_rate):
        for epoch in range(num_epochs):
            for image in positive_examples:
                prediction = self.predict(image)
                # Update weights and bias
                error = 1 - prediction  # Error is 1 if prediction is 0 (i.e., negative), 0 if prediction is 1 (i.e., positive)
                self.weights += learning_rate * error * image.flatten()
                self.bias += learning_rate * error

    def get_name(self):
        return self.name

    def get_confidence(self, image):
        # Flatten the image matrix into a 1D array
        flattened_image = image.flatten()
        
        # Compute the weighted sum
        weighted_sum = np.dot(flattened_image, self.weights) + self.bias
        
        # Apply activation function (Step function)
        confidence = weighted_sum
        return confidence
