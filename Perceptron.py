import numpy as np

class Perceptron:
    def __init__(self, name, height, width):
        self.name = name
        self.height = height;
        self.width = width;
        self.weights = np.random.rand(height*width)
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
        height = image.shape[0]
        width = image.shape[1]

        data_height = self.height
        data_width = self.width

        print(height)
        print(width)
        print(data_height)
        print(data_width)

        for x in range(0, width, data_width):
            if x >= data_width:
                break
            for y in range(0, height, data_height):
                if y >= data_height:
                    break
                confidence = self.helper_confidence(image[height - data_height: height, width - data_width: width])

        return confidence

    def helper_confidence(self, image):
        # Flatten the image matrix into a 1D array
        flattened_image = image.flatten()

        print(flattened_image)
        
        # Compute the weighted sum
        weighted_sum = np.dot(flattened_image, self.weights) + self.bias
        
        # Apply activation function (Step function)
        confidence = weighted_sum
        return confidence
