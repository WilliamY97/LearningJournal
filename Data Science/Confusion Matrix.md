# Confusion Matrix

An NxN table that summarizes how successful a **classification model's** predictions were, that is, the correlation
between the label and the model's classificaiton. On one axis is the label the model predicted and the
other axis is the actual label. N represents the number of classes.

Ex. Binary Classification problem, N=2. 


![alt tag](http://www.dataschool.io/content/images/2015/01/confusion_matrix_simple2.png)

## Application of Confusion Matrix

The Confusion Matrix of a multi-class confusion matrix can help you determine mistake patterns. For
example, a confusion matrix could reveal that a model trained to recognize handwritten digits tends
to mistakenly predict 9 instead of 4, or 1 instead of 7.

It also contains enough infomration to calculate a variety of performanc metrics, including precision
and recall.
