# Categorical Cross-Entropy

Using the sum of squared errors as the cost function in our networks is good, but in singular (scalar) output values. When you're using
softmax, however your output is a vector. One vector is the probability values from the output units. You can also express your data
labels as a vector using what's called **one-hot encoding**

This just means that you have a vector the length of the number of classes, and the label element is marked with a 1 while the other
labels are set to 0.

Example: Label vector from image of 4 is y=[0,0,0,0,1,0,0,0,0,0]

Prediction Vector = [0.047,0.048,0.061,0.07,0.330,0.062,0.001,0.213,0.013,0.150]

We want our error to be proportional to how far apart these vectors are. To calculate this distance, we'll use the **cross entropy**. Then, our goal when training the network is to make our prediction vectors as close as possible to the label vectors by minimizing the cross entropy. The cross entropy calculation is shown below:
