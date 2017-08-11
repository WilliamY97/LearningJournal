# Tensor Flow

## About

An open-source software library for Machine Intelligence

## Tensor
In TensorFlow, data isn’t stored as integers, floats, or strings. These values are encapsulated in an object called a tensor. In the case of ```hello_constant = tf.constant('Hello World!')```, hello_constant is a 0-dimensional string tensor, but tensors come in a variety of sizes as shown below:

```
# A is a 0-dimensional int32 tensor
A = tf.constant(1234) 
# B is a 1-dimensional int32 tensor
B = tf.constant([123,456,789]) 
 # C is a 2-dimensional int32 tensor
C = tf.constant([ [123,456,789], [222,333,444] ])
```

## Session

A "TensorFlow Session", is an environment for running a graph. The session is in charge of allocating the operations to GPU(s) and/or CPU(s), including remote machines.

```
with tf.Session() as sess:
    output = sess.run(hello_constant)
```
## Session’s feed_dict and tf.placeholder()

Use the feed_dict parameter in tf.session.run() to set the placeholder tensor. It's also possible to set more than one tensor using feed_dict as shown below.

```
x = tf.placeholder(tf.string)
y = tf.placeholder(tf.int32)
z = tf.placeholder(tf.float32)

with tf.Session() as sess:
    output = sess.run(x, feed_dict={x: 'Test String', y: 123, z: 45.67})
```
