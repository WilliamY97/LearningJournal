# Multilayer Perceptrons

Before, dealing with only one output node which made the code straightforward. However now that we have multiple input units and multiple hidden units, the weights between them will require two indices. W(ij) where i denots input units and j are the hidden units.

![alt tag](http://neuroph.sourceforge.net/tutorials/images/MLP.jpg)

An XOR perceptron is a logic gate that outputs 0 if the inputs are the same and 1 if the inputs are different. 
Unlike previous perceptrons, this graph isn't linearly separable. To handle more complex problems like this, 
we can chain perceptrons together.

