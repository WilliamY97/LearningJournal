# Naive Bayes

Naive Bayes is a classification technique based on Bayes' Theorem with an assumption of independence amongst predictors. In simple terms,
a Naive Bayes classifier assumes that the presence of a particular feature in a class is unrelated to any other feature.

Ex. *A fruit may be considered to be an apple if it is red, round, and about 3 inches in diameter. Even if these features depend on each other or upon the existence of the other features, all of these properties independently contribute to the probability that this fruit is an apple and that is why it is known as ‘Naive’.*

![alt tag](http://www.saedsayad.com/images/Bayes_rule.png)

### Definitions

P(c|x) - Posterior probability of class given predictor

P(c) - Prior probability of class

P(x|c) - Likelihood which is the probability of predictor given class

P(x) - Prior probability of predictor

## Pros and Cons

### Pros

- It is easy and fast to predict class of test data set. It also performs well in multi-class predictions
- When assumption of independence holds, a Naive Bayes classifier performs better compared to other models like logistic
regression and you need less training data.

### Cons

- If categorical variable has a category (in test data set), which was not observed in training data set, then model assign
a 0 probability and will be unable to make a prediction. This is often known as Zero Frequency.
- Naive Bayes is known as a bad estimator, so the probability outputs from are not taken as seriously.
- Limitation of NB is the assumption of independent predictors. In real life, it is almost impossible that we get a set
of predictor which are completely independent.
