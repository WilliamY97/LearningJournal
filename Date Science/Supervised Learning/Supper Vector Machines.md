# Support Vector Machines (SVM)

Support Vector Machines (aka Support Vector Networks) are a type of supervised learning model used for classification and regression analysis.

![alt tag](https://upload.wikimedia.org/wikipedia/commons/thumb/f/fe/Kernel_Machine.svg/512px-Kernel_Machine.svg.png)

Simply speaking, the SVM model is a representation of the data as points in space, seperated by a gap that is as wide as possible. New
examples can then be added to the space and predicted to belong to a category based on which side of the gap they fall on.

*Support Vector Machines are an optimization problem. They are attempting to find a hyperplane that divides the two classes with the largest margin. The support vectors are the points which fall within this margin. It's easiest to understand if you build it up from simple to more complex.*

## Definitons

### Kernel
A kernel is a similarity function. It is a function that you, as the domain expert, provide to a machine learning algorithm. It takes two inputs and spits out how similar they are. Suppose your task is to learn to classify images. You have (image, label) pairs as training data.


## Hard Margin Linear SVM

![alt tag](https://i.stack.imgur.com/qt3CZ.png)

In a training set where the data is linearly seperable, we can use a hard margin (no slack) and the support vectors are the points
that lie along the supporting hyperplanes (the hyperplanes parallel to the dividing hyperplane at the edges of the margin). 

## Soft-Margin Linear SVM

![alt tag](https://i.stack.imgur.com/npEOk.png)

In the case that the set is not linearly seperable, we use soft-margin which allows for data points to be within the margin. We use the slack parameter C to control this. (nu in nu-SVM). This gives us a wider margin and greater error on the training dataset, but improves generalization. 

The soft-margin is a implementation that allows us to find a linear separation of data that is not linearly separable.

## Non-Linear SVM

![alt tag](https://i.stack.imgur.com/1gvce.png)

The data set may not have a linear relationship in a specific dimension, but we can still find a linear relationship in a higher
dimensional space. 

The number of support vectors still depends on how much slack we allow, but it also depends on the complexity of our model.

The output of an SVM is the support vectors and an alpha, which is defining how much influence that specific support vector has on
the final decision.

