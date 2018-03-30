# InterpolationGeneration
A stupidly simple "generative model" tested on standard univariate distributions and the MNIST dataset.

#### Method
Estimate the empirical distribution of the training set. Generate a uniform random variable _u_ between 0 and 1. Find the value at the _u_'th percentile of the training set, linearly interpolating when the desired quantile lies between two data points. That's it!

![Empirical Distribution](examples/empdistrib.png)

## Results
### Gaussian
![Gaussian](examples/univariate_gaussian_examples.png)

### Exponential
![Univariate](examples/univariate_exp_examples.png)

### MNIST
For each of the 784 pixels in an MNIST image, consider the ECDF of the distribution of that pixel's values across all images in the training set with the same label. Sample a new value from this distribution using the method described above. Note that this strategy does not incorporate the prior knowledge that pixels near each other should be related to one another. This method is stupid!

![MNIST](examples/mnist_example_1.png)
![MNIST](examples/mnist_example_2.png)
![MNIST](examples/mnist_example_3.png)
![MNIST](examples/mnist_example_4.png)
![MNIST](examples/mnist_example_5.png)
![MNIST](examples/mnist_example_6.png)
![MNIST](examples/mnist_example_7.png)
![MNIST](examples/mnist_example_8.png)
![MNIST](examples/mnist_example_9.png)
