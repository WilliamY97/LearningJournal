# Back Propogation

![alt tag](https://www.researchgate.net/profile/Alimorad_Rashidi/publication/260063112/figure/fig4/AS:214336464265219@1428113203630/A-three-layered-FFNN-with-a-backpropagation-training-algorithm.png)

To update the weights to hidden layers using gradient descent, we need to know how much error each of the hidden units
contributed to the final output. Since the output of a layer is determined by the weights between layers, the error 
resulting from units is scaled by the weights going forward through the network. **Since we know the error at the output,
we can use the weights to work backwards to hidden layers.**

Essentially we want to take the output error and check how much error the hidden layer perceptrons contribute so that we can then go and optimize those weights as well. This is done by error = output error * weight * gradient.

## Problems with the Sigmoid Activation Function

The maximum derivative of the sigmoid function is 0.25, so the errors in the output layer get reduced by at least 75%, and errors in the hidden layer are scaled down by at least 93.75%!

You can see that if you have a lot of layers, using a sigmoid activation function will quickly reduce the weight steps to tiny values in layers near the input . This is known as the **vanishing gradient problem**. Later in the course you'll learn about other activation functions that perform better in this regard and are more commonly used in modern network architectures.

![alt tag](https://cdn-images-1.medium.com/max/1600/1*gkXI7LYwyGPLU5dn6Jb6Bg.png)

