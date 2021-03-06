# Multilayer Perceptrons

Adding more layers to a neural network allows us to model **linearly inseperable data**, impossible to do with regression models.

Before, dealing with only one output node which made the code straightforward. However now that we have multiple input units and multiple hidden units, the weights between them will require two indices. W(ij) where i denots input units and j are the hidden units.

<img src="https://d17h27t6h515a5.cloudfront.net/topher/2017/February/589978f4_network-with-labeled-weights/network-with-labeled-weights.png" width="500" height="400" />

Before, we were able to write the weights as an array, indexed as w(i).

But now, the weights need to be stored in a matrix, indexed as w(ij). Each row in the matrix will correspond to the weights leading out of a single input unit, and each column will correspond to the weights leading in to a single hidden unit. For our three input units and two hidden units, the weights matrix looks like this:

<img src="https://d17h27t6h515a5.cloudfront.net/topher/2017/February/58a49908_multilayer-diagram-weights/multilayer-diagram-weights.png" width="500" height="200" />

To initialize these weights in Numpy, we have to provide the shape of the matrix. If features is a 2D array containing the input data:

```
# Number of records and input units
n_records, n_inputs = features.shape
# Number of hidden units
n_hidden = 2
weights_input_to_hidden = np.random.normal(0, n_inputs**-0.5, size=(n_inputs, n_hidden))
```

<img src="https://d17h27t6h515a5.cloudfront.net/topher/2017/January/588ae392_codecogseqn-2/codecogseqn-2.png" width="200" height="20" />

