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

## Initialization

```
init = tf.global_variables_initializer()
with tf.Session() as sess:
    sess.run(init)
```

The ```tf.global_variables_initializer()``` call returns an operation that will initialize all TensorFlow variables from the graph. You call the operation using a session to initialize all the variables as shown above. Using the ```tf.Variable``` class allows us to change the weights and bias, but an initial value needs to be chosen.

Initializing the weights with random numbers from a normal distribution is good practice. Randomizing the weights helps the model from becoming stuck in the same place every time you train it.

Similarly, choosing weights from a normal distribution prevents any one weight from overwhelming other weights. You'll use the ```tf.truncated_normal()``` function to generate random numbers from a normal distribution.
