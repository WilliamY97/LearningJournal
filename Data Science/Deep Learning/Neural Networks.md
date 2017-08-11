# Neural Networks

## Perceptron

Data, like test scores and grades, is fed into a network of interconnected nodes.
These individual nodes are called perceptrons or neurons, and they are the basic unit of a neural network.
Each one looks at input data and decides how to categorize that data.

### How a Perceptron Processes Input Data

When input data comes into a perceptron, it gets multiplied by a weight value that is assigned to this particular input.

These weights start out as random values, and as the neural network learns more about what kind of input data leads to a student being accepted into a university, the network adjusts the weights based on any errors in categorization that the previous weights resulted in. This is called **training** the neural network.

A higher weight means the neural network considers that input more important than other inputs, and lower weight means that the data is considered less important.

## Summing the Input Data

So, each input to a perceptron has an associated weight that represents its importance and these weights are determined during the learning process of a neural network, called training.

The weighted input data is then summed up and the result determines the final output.

The perceptron applies these weights to the inputs and sums them in a process known as a **linear combination**.
