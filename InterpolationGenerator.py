import numpy as np

class InterpolationGenerator:

    def __init__(self):
        pass

    def train(self, training_data):
        self.training_data = training_data

    def generate(self, num_samples):
        new_samples = np.random.uniform(low=0.0, high=1.0, size=num_samples)
        for i in range(len(new_samples)):
            new_samples[i] = np.percentile(self.training_data, 100*new_samples[i], interpolation = 'linear')
        return new_samples
