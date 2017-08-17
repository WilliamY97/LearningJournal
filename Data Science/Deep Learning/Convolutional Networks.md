# Convolutional Networks

Notes taken from the source https://ujjwalkarn.me/2016/08/11/intuitive-explanation-convnets/ which is an incredible explanation of the
steps for CovNets.

![alt tag](https://ujwlkarn.files.wordpress.com/2016/08/conv_all.png?w=748)

Convolutional Networks are neural networks that share their parameters across space.

If the data has some structure, and the neural network doesn't have to learn that structure from scratch, it's going to perform better.
For example in classifying letters, the attribute of color does not play a role in what makes an A an A.

There are four main operations in the ConvNet:

1. Convolution
2. Non Linearity (ReLU)
3. Pooling or Sub Sampling
4. Classification (Fully Connected Layer)

## Important Concepts

**Translation Invariance:** Showing explicitly, that objects and images are largely the same whether or not they are on the left or on the right of the picture.

**Weight Sharing:** When you know two inputs can contain the same kind of information, then you join their weights and train the weights
jointly for those inputs.

## Application to Images

Channel is a conventional term used to refer to a certain component of an image. An image from a standard digital camera will have three channels – red, green and blue – you can imagine those as three 2d-matrices stacked over each other (one for each color), each having pixel values in the range 0 to 255.

A grayscale image, on the other hand, has just one channel. We only consider grayscale images, since they are easier for your classifier to
learn. So we will have a single 2d matrix representing an image. The value of each pixel in the matrix will range from 0 to 255 – zero indicating black and 255 indicating white.

## Application of the Non Linearity (ReLU)

The ReLU activation function is used after every Convolution operation. ReLU is an element wise operation (applied per pixel) and replaces all negative pixel values in the feature map by zero. The purpose of ReLU is **to introduce non-linearity in our ConvNet, since most of the real-world data we would want our ConvNet to learn would be non-linear** (Convolution is a linear operation – element wise matrix multiplication and addition, so we account for non-linearity by introducing a non-linear function like ReLU).

![alt tag](https://ujwlkarn.files.wordpress.com/2016/08/screen-shot-2016-08-07-at-6-18-19-pm.png?w=748)


## The Convolution Step

![alt tag](https://ujwlkarn.files.wordpress.com/2016/07/convolution_schematic.gif?w=268&h=196)

The figure above displays the Convolution operation. The output matrix is called **Convolved Feature or Feature Map**.

We slide the orange matrix over our original matrix by 1 pixel (called stride) and for every position, we compute element
wise multiplication (between two matrices) and add the multiplication outputs to get the final integer which forms a single
element of the output matrix (pink). The 3x3 matrix "sees" only a part of the input image in each stride.

In CNN terminology, the 3×3 matrix is called a ‘filter‘ or ‘kernel’ or ‘feature detector’ and the matrix formed by sliding the filter over the image (in the form of input matrix) and computing the dot product is called the ‘Convolved Feature’ or ‘Activation Map’ or the ‘Feature Map‘. It is important to note that filters acts as feature detectors from the original input image.

In the table below, we can see the effects of convolution of the above image with different filters. As shown, we can perform operations such as Edge Detection, Sharpen and Blur just by changing the numeric values of our filter matrix before the convolution operation.

![alt tag](https://ujwlkarn.files.wordpress.com/2016/08/screen-shot-2016-08-05-at-11-03-00-pm.png?w=342&h=562)

### Steps before Convolution

The size of the Feature Map (Convolved Feature) is controlled by three parameters that we need to decide before convolution.

**Depth:** Depth corresponds to the number of filters we use for the convolution operation. We can for example, use three
distinct filters, to create three different feature maps. You can think of these three feature maps as stacked 2d matrices, so,
the 'depth' of the feature map would be three.

**Stride:** Stride is the number of pixels by which we slide our filter matrix over the input matrix. When the stride is 1 then
we move the filters one pixel at a time. When the stride is 2, then the filters jump 2 pixels at a time as we slide them around.
Having a larger stride will produce smaller feature maps.

**Zero-Padding:** Sometimes, it is convenient to pad the input matrix with zeros around the border, so that we can apply the filter to bordering elements of our input image matrix. A nice feature of zero padding is that it allows us to control the size of the feature maps. Adding zero-padding is also called **wide convolution**, and not using **zero-padding** would be a narrow convolution.

### How do we know which filter to apply??

In practice, a CNN learns the values of these filters on its own during the training process (although we still need to specify parameters such as number of filters, filter size, architecture of the network etc. before the training process). The more number of filters we have, the more image features get extracted and the better our network becomes at recognizing patterns in unseen images.

## The Pooling Step

**Spatial Pooling** (also called subsampling or downsampling) reduces the dimensionality of each feature map but retains the most important information. Spatial Pooling can be of different types: Max, Average, Sum etc.

In case of **Max Pooling**, we define a spatial neighborhood (for example, a 2×2 window) and take the largest element from the rectified feature map within that window. Instead of taking the largest element we could also take the average (Average Pooling) or sum of all elements in that window. In practice, Max Pooling has been shown to work better.

![alt tag](https://ujwlkarn.files.wordpress.com/2016/08/screen-shot-2016-08-10-at-3-38-39-am.png?w=494)

**Note**: Pooling operation is applied seperately to each feature map (notice that, due to this, we get three output maps from three input maps).

### What is the Purpose of Pooling

The function of Pooling is to progressively reduce the spatial size of the input representation. In particular, pooling

- makes the input representations (feature dimension) smaller and more manageable
- reduces the number of parameters and computations in the network, therefore, controlling overfitting
- makes the network invariant to small transformations, distortions and translations in the input image (a small distortion in input will not change the output of Pooling – since we take the maximum / average value in a local neighborhood).
- helps us arrive at an almost scale invariant representation of our image (the exact term is “equivariant”). This is very powerful since we can detect objects in an image no matter where they are located.

## Big Picture

![alt tag](https://ujwlkarn.files.wordpress.com/2016/08/screen-shot-2016-08-08-at-2-26-09-am.png?w=748)

## Fully Connected Layer

The Fully Connected layer is a traditional Multi Layer Perceptron that uses a softmax activation function in the output layer (other classifiers like SVM can also be used, but will stick to softmax in this post). The term “Fully Connected” implies that every neuron in the previous layer is connected to every neuron on the next layer.

![alt tag](https://ujwlkarn.files.wordpress.com/2016/08/screen-shot-2016-08-06-at-12-34-02-am.png?w=484&h=152)

The output from the convolutional and pooling layers represent high-level features of the input image. The purpose of the Fully Connected layer is to use these features for classifying the input image into various classes based on the training dataset.

Apart from classification, adding a fully-connected layer is also a (usually) cheap way of learning non-linear combinations of these features. Most of the features from convolutional and pooling layers may be good for the classification task, but combinations of those features might be even better.

The sum of output probabilities from the Fully Connected Layer is 1. This is ensured by using the Softmax as the activation function in the output layer of the Fully Connected Layer. The Softmax function takes a vector of arbitrary real-valued scores and squashes it to a vector of values between zero and one that sum to one.

## Putting Everything Together

As discussed above, the Convolution + Pooling layers act as Feature Extractors from the input image while Fully Connected layer acts as a classifier.

![alt tag](https://ujwlkarn.files.wordpress.com/2016/08/screen-shot-2016-08-07-at-9-15-21-pm.png?w=748)

- Step1: We initialize all filters and parameters / weights with random values
- Step2: The network takes a training image as input, goes through the forward propagation step (convolution, ReLU and pooling operations along with forward propagation in the Fully Connected layer) and finds the output probabilities for each class.
Lets say the output probabilities for the boat image above are [0.2, 0.4, 0.1, 0.3]
Since weights are randomly assigned for the first training example, output probabilities are also random.
- Step3: Calculate the total error at the output layer (summation over all 4 classes)
 Total Error = ∑  ½ (target probability – output probability) ²
- Step4: Use Backpropagation to calculate the gradients of the error with respect to all weights in the network and use gradient descent to update all filter values / weights and parameter values to minimize the output error.
The weights are adjusted in proportion to their contribution to the total error.
When the same image is input again, output probabilities might now be [0.1, 0.1, 0.7, 0.1], which is closer to the target vector [0, 0, 1, 0].
This means that the network has learnt to classify this particular image correctly by adjusting its weights / filters such that the output error is reduced.
Parameters like number of filters, filter sizes, architecture of the network etc. have all been fixed before Step 1 and do not change during training process – only the values of the filter matrix and connection weights get updated.
- Step5: Repeat steps 2-4 with all images in the training set.
