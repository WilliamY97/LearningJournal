# Categorical Cross-Entropy

Using the sum of squared errors as the cost function in our networks is good, but in singular (scalar) output values. When you're using
softmax, however your output is a vector. One vector is the probability values from the output units. You can also express your data
labels as a vector using what's called **one-hot encoding**

This just means that you have a vector the length of the number of classes, and the label element is marked with a 1 while the other
labels are set to 0.

Example: Label vector from image of 4 is y = [0,0,0,0,1,0,0,0,0,0]

Prediction Vector = [0.047,0.048,0.061,0.07,0.330,0.062,0.001,0.213,0.013,0.150]

We want our error to be proportional to how far apart these vectors are. To calculate this distance, we'll use the **cross entropy**. Then, our goal when training the network is to make our prediction vectors as close as possible to the label vectors by minimizing the cross entropy. As seen below:

![alt tag](https://d17h27t6h515a5.cloudfront.net/topher/2017/February/589b18f5_cross-entropy-diagram/cross-entropy-diagram.png)

As you can see above, the cross entropy is the sum of the label elements times the natural log of the prediction probabilities. Note that this formula is not symmetric! Flipping the vectors is a bad idea because the label vector has a lot of zeros and taking the log of zero will cause an error.

What's good about one-hot encoding is that everything in the label vector for Yj is 0 except for the one true class. Then, all terms in
that sum except for where Yj = 1 are zero and the cross entropy is simply D = -ln(prediction vector) for the true label. For example, if
your input image is 4 and it's labeled 4, then only the output of the unit corresponding to 4 matters in the cross entropy cost.

## Cross Entropy in TensorFlow

As with the softmax function, TF has a function to do the cross entropy calculations.

## Minimizing Cross Entropy

One thing you can do is measure that distance averaged over the entire training sets for all the inputs and all the labels that you have available. That's called the training loss. This loss, which is the average cross-entropy over your entire training set, Is one humongous function. Every example in your training set gets multiplied by this one big matrix W. And then they get all added up in one big sum.
We want all the distances to be small, which would mean we're doing a good job at classifying every example in the training data. So we want the loss to be small. The loss is a function of the weights and the biases. So we are simply going to try and minimize that function.


