# Multilayer Perceptrons

Before, dealing with only one output node which made the code straightforward. However now that we have multiple input units and multiple hidden units, the weights between them will require two indices. W(ij) where i denots input units and j are the hidden units.

<img src="https://d17h27t6h515a5.cloudfront.net/topher/2017/February/589978f4_network-with-labeled-weights/network-with-labeled-weights.png" alt="Drawing" style="height: 100px; width:100px;"/>

An XOR perceptron is a logic gate that outputs 0 if the inputs are the same and 1 if the inputs are different. 
Unlike previous perceptrons, this graph isn't linearly separable. To handle more complex problems like this, 
we can chain perceptrons together.

