# Convolutional Networks

Notes taken from the source https://ujjwalkarn.me/2016/08/11/intuitive-explanation-convnets/ which is an incredible explaination of the
steps for CovNets.

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



