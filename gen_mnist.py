import numpy as np
import matplotlib.pyplot as plt

from InterpolationGenerator import InterpolationGenerator
from tensorflow.examples.tutorials.mnist import input_data

# Load MNIST Dataset
mnist = input_data.read_data_sets("data/")

# Filter to only include images of 8
character_eight_images = []
for label, image in zip(mnist.train.labels, mnist.train.images):
    if label == 8:
        character_eight_images.append(image)

character_eight_images = np.array(character_eight_images)

# Set up data structure to hold new samples
num_samples = 1
new_samples = np.zeros((num_samples, character_eight_images.shape[1]))

# Generate new samples from distribution of every pixel
for i in range(character_eight_images.shape[1]):
    pixel_dist = character_eight_images[:, i]

    # Train model
    generator = InterpolationGenerator()
    generator.train(pixel_dist)

    # Generate new samples from that pixel's distribution
    new_samples[:, i] = generator.generate(num_samples)

# Plot samples
figure = plt.figure(figsize=(5, 10))

real_ax = plt.subplot(2, 1, 1)
real_ax.set_title('REAL')
real_ax.imshow(character_eight_images[0].reshape(28,28))

syn_ax = plt.subplot(2, 1, 2)
syn_ax.set_title('SYNTHETIC')
syn_ax.imshow(new_samples[0].reshape(28,28))

figure.savefig('OUTPUT/mnist_examples.png')
plt.close()
