# ReLU and Softmax Activation Functions

Previously, I've been using the sigmoid function as the activation function on hidden layers, in the case of classification, on the
output unit. Howeve, this is not the only activation function, and it also has drawbacks.

![alt tag](https://d17h27t6h515a5.cloudfront.net/topher/2017/February/5893d15c_sigmoids/sigmoids.png)

As mentioned in my other notes, the derivative of the sigmoid function maxes out at 0.25. This means when performing **back propogation** with sigmoid units, the errors going back into the network will be shrunk by at least 75% at every layer. For layers close to the input layer, the weight updates will be tiny if you have a lot of layers and those weights will take a really long time to train. **Due to this, sigmoids have fallen out of favor as activations on hidden units.**

## Rectified Linear Units (The New Popular Activation Function)

Instead of sigmoids, most recent deep learning networks use **rectified linear units (ReLUs)** for the hidden layers. A rectified linear
unit has output 0 if the input is less than 0, and raw output otherwise. That is, if the input is greater than 0, the output is equal to
the input. Mathematically this is f(x) = max(x,0).

The output of the function is either the input x, or 0, whichever is larger. So if x = -1, then f(x) = 0 and if x = 0.5 then f(x) = 0.5.
Graphically, it looks like:

![alt tag](https://d17h27t6h515a5.cloudfront.net/topher/2017/February/58915ae8_relu/relu.png)

ReLU activations are the simplest non-linear activation function you can use. When the input is positive, the derivative is 1, so there isn't the vanishing effect you see on backpropagated errors from sigmoids. Research has shown that ReLUs result in much faster training for large networks. Most frameworks like TensorFlow and TFLearn make it simple to use ReLUs on the the hidden layers, so you won't need to implement them yourself.

# Drawbacks

It's possible that a large gradient can set the weights such that a ReLU units will always be 0. These "dead" units will always be
0 and a lot of computation will be wasted in training.

CS231 Quote:

*
Unfortunately, ReLU units can be fragile during training and can “die”. For example, a large gradient flowing through a ReLU neuron could cause the weights to update in such a way that the neuron will never activate on any datapoint again. If this happens, then the gradient flowing through the unit will forever be zero from that point on. That is, the ReLU units can irreversibly die during training since they can get knocked off the data manifold. For example, you may find that as much as 40% of your network can be “dead” (i.e. neurons that never activate across the entire training dataset) if the learning rate is set too high. With a proper setting of the learning rate this is less frequently an issue.
*
