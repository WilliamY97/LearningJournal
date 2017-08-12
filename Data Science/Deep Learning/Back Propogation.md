# Back Propogation

To update the weights to hidden layers using gradient descent, we need to know how much error each of the hidden units
contributed to the final output. Since the output of a layer is determined by the weights between layers, the error 
resulting from units is scaled by the weights going forward through the network. **Since we know the error at the output,
we can use the weights to work backwards to hidden layers.**

