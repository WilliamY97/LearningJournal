# Back Propogation

To update the weights to hidden layers using gradient descent, we need to know how much error each of the hidden units
contributed to the final output. Since the output of a layer is determined by the weights between layers, the error 
resulting from units is scaled by the weights going forward through the network. **Since we know the error at the output,
we can use the weights to work backwards to hidden layers.**

You can see that if you have a lot of layers, using a sigmoid activation function will quickly reduce the weight steps to tiny values in layers near the input. This is known as the **vanishing gradient problem**. Later in the course you'll learn about other activation functions that perform better in this regard and are more commonly used in modern network architectures.
