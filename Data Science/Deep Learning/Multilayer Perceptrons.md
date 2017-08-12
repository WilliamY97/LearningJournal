# Multilayer Perceptrons

Before, dealing with only one output node which made the code straightforward. However now that we have multiple input units and multiple hidden units, the weights between them will require two indices. W(ij) where i denots input units and j are the hidden units.

<img src="https://d17h27t6h515a5.cloudfront.net/topher/2017/February/589978f4_network-with-labeled-weights/network-with-labeled-weights.png" width="500" height="400" />

But now, the weights need to be stored in a matrix, indexed as w(ij). Each row in the matrix will correspond to the weights leading out of a single input unit, and each column will correspond to the weights leading in to a single hidden unit. For our three input units and two hidden units, the weights matrix looks like this:

<img src="https://d17h27t6h515a5.cloudfront.net/topher/2017/February/58a49908_multilayer-diagram-weights/multilayer-diagram-weights.png" width="500" height="200" />

