# Categorical Cross-Entropy

Using the sum of squared errors as the cost function in our networks is good, but in singular (scalar) output values. When you're using
softmax, however your output is a vector. One vector is the probability values from the output units. You can also express your data
labeles as a vector using what's called **one-hot encoding**

This just means that you have a vector the length of the number of classes, and the label element is marked with a 1 while the other
labels are set to 0.

