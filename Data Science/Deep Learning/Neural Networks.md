# Neural Networks

# Perceptron

![alt tag](https://i.stack.imgur.com/KUvpQ.png)

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

## Calculating the Output with an Activation Function

Finally, the result of the perceptron's summation is turned into an output signal. This is done by feeding the linear combination into an **activation function**.

Activation functions are functions that decide, given the inputs into the node, what should be the node's output? Because it's the activation function that decides the actual output, we often refer to the outputs of a layer as its "activations".

One of the simplest activation functions is the **Heaviside step function**. This function returns a 0 if the linear combination is less than 0. It returns a 1 if the linear combination is positive or equal to zero.

![alt tag](https://d17h27t6h515a5.cloudfront.net/topher/2017/February/5895102f_heaviside-step-function-2/heaviside-step-function-2.gif)

### Getting more inputs to result in the expected output

One way to get our function to return 1 for more inputs is to add a value to the results of our linear combination, called a **bias**.

A bias, represented in equations as b, lets us move values in one direction or another.

Of course, with neural networks we won't know in advance what values to pick for biases. That’s ok, because just like the weights, the bias can also be updated and changed by the neural network during training. So after adding a bias, we now have a complete perceptron formula:

![alt tag](https://d17h27t6h515a5.cloudfront.net/topher/2017/February/58951180_perceptron-equation-2/perceptron-equation-2.gif)

Then the neural network starts to learn! Initially, the weights and bias are assigned a random value, and then they are updated using a learning algorithm like gradient descent. The weights and biases change so that the next training example is more accurately categorized, and patterns in data are "learned" by the neural network.

## Simplest Neural Network

Other activation functions are the logistic (ex. the sigmoid), tanh, and softmax functions. Mostly use of the sigmoid function.

```sigmoid(x)=1/(1+e^−x)```

The sigmoid function is bounded between 0 and 1, and as an output can be interpreted as a probability for success. It turns out, again, using a sigmoid as the activation function results in the same formulation as logistic regression.

This is where it stops being a perceptron and begins being called a neural network. In the case of simple networks like this, neural networks don't offer any advantage over general linear models such as logistic regression.

Using activation functions that are continuous and differentiable, it's possible to train the network using gradient descent, which you'll learn about next.
