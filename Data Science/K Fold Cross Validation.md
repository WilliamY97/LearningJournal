# K Fold Cross Validation

Normally we seperate our data into a training and testing set, but this is not ideal as **we are not using some of the data for our training**. For K Fold Cross Validation we break our data into buckets (K buckets). Then we train our model K times, using a different bucket each time and using all other remaining points from buckets as our testing set. Finally we average the results of all the training sets to get a final model.

## Cross Validation in SKLearn

```
from sklearn.model_selection import KFold
kk = kFold(12,3)

for train_indices, test_indices in kf:
  print train_indices, test_indices
```

## Randomizing in Cross Validation
It is always recommended to randomize data to remove any hint of bias.

Here we are still splitting our data into buckets except there are chosen randomly instead of in order.

Randomizing is also easily done in sklearn by setting the shuffle parameter to be true when we initialize our KFold object.

```
kf = kFold(12, 3, shuffle = True)
```

