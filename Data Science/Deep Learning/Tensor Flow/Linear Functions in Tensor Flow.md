# Linear Functions in Tensor Flow

The most common operation in neural networks is calculating the linear combination of inputs, weights, and biases. As a reminder, we can
write the output of the linear operation as y = xW + b

## Weights and Bias in TensorFlow

The goal of training a neural network is to modify weights and biases to best predict the labes. In order to use weights and bias, you'll
need a Tensor that can be modified. This leaves out ```tf.placeholder()``` and ```tf.constant()```, since those Tensors can't be modified.
This is where ```tf.variable``` class comes in.

The tf.Variable class creates a tensor with an initial value that can be modified, much like a normal Python variable. 
This tensor stores its state in the session, so you must initialize the state of the tensor manually. 
You'll use the ```tf.global_variables_initializer()``` function to initialize the state of all the Variable tensors.
