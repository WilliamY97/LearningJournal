# Back Propogation

![alt tag](https://jamesmccaffrey.files.wordpress.com/2012/11/backpropagationcalculations.jpg)

To update the weights to hidden layers using gradient descent, we need to know how much error each of the hidden units
contributed to the final output. Since the output of a layer is determined by the weights between layers, the error 
resulting from units is scaled by the weights going forward through the network. **Since we know the error at the output,
we can use the weights to work backwards to hidden layers.**

he maximum derivative of the sigmoid function is 0.25, so the errors in the output layer get reduced by at least 75%, and errors in the hidden layer are scaled down by at least 93.75%!

You can see that if you have a lot of layers, using a sigmoid activation function will quickly reduce the weight steps to tiny values in layers near the input . This is known as the **vanishing gradient problem**. Later in the course you'll learn about other activation functions that perform better in this regard and are more commonly used in modern network architectures.
