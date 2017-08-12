# Gradient Descent

We want the network's prediction error to be as small as possible and the weights are the knobs we adjust to make this true. Our goal is to find weights that minimize the squared error. To achieve this we need to use **Gradient Descent**.

The models we create will need learn to adjust the weights from example data, then use those weights to make the predictions.

To figure out how we're going to find these weights, start by thinking about the goal. We want the network to make predictions as close as possible to the real values. To measure this, we need a metric of how wrong the predictions are, the error. A common metric is the sum of the **squared errors (SSE)**:

The SSE is a good choice for a few reasons. The square ensures the error is always positive and larger errors are penalized more than smaller errors.

