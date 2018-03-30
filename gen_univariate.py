import numpy as np
import matplotlib.pyplot as plt

from InterpolationGenerator import InterpolationGenerator

# Load dataset
train_data = np.random.normal(loc=0.0, scale=1.0, size=1000)

# Train model
generator = InterpolationGenerator()
generator.train(train_data)

# Generate new samples
new_samples = generator.generate(1000)

# Plot samples
figure = plt.figure(figsize=(5, 10))

real_ax = plt.subplot(2, 1, 1)
real_ax.set_title('REAL')
real_ax.hist(train_data, density=True)

syn_ax = plt.subplot(2, 1, 2)
syn_ax.set_title('SYNTHETIC')
syn_ax.hist(new_samples, density=True)

figure.savefig('OUTPUT/univariate_examples.png')
plt.close()
