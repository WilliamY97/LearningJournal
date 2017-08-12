# Gradient Descent

We want the network's prediction error to be as small as possible and the weights are the knobs we adjust to make this true. Our goal is to find weights that minimize the squared error. To achieve this we need to use **Gradient Descent**.

The models we create will need learn to adjust the weights from example data, then use those weights to make the predictions.

To figure out how we're going to find these weights, start by thinking about the goal. We want the network to make predictions as close as possible to the real values. To measure this, we need a metric of how wrong the predictions are, the error. A common metric is the sum of the **squared errors (SSE)**:

The SSE is a good choice for a few reasons. The square ensures the error is always positive and larger errors are penalized more than smaller errors.

## How It Works

At each step, you calculate the error and the gradient, then use those to determine how much to change each weight. Repeating this process will eventually find weights that are close to the minimum of the error function, the block dot in the middle.

With gradient descent, we take multiple small steps towards our goal. In this case, we want to change the weights in steps that reduce the error. Since the fastest way down is in the steepest direction, the steps taken should be in the direction that minimizes the error the most. We can find this direction by calculating the **gradient** of the squared error.

**Gradient** is another term for rate of change or slope.

The gradient is just a derivative generalized to functions with more than one variable. We can use calculus to find the gradient at any point in our error function, which depends on the input weights. You'll see how the gradient descent step is derived on the next page.

![alt tag](https://d17h27t6h515a5.cloudfront.net/topher/2017/January/587ba606_gradient-descent/gradient-descent.png)

