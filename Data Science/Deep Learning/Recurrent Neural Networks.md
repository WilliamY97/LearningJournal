# Recurrent Neural Networks

The core of these notes have been taken from reading the blog post http://colah.github.io/posts/2015-08-Understanding-LSTMs/

Traditional neural networks do not address the concept of persistence. The idea that you don't throw everything you understood
before away and start thinking from scratch again. Recurrent neural networks address this issue, they are networks with loops
in them, allowing for information to persist.

![alt tag](http://colah.github.io/posts/2015-08-Understanding-LSTMs/img/RNN-unrolled.png)

The figure above shows an unrolled recurrent neural network.

## Problem of Long-Term Dependencies

One of the appeals of RNNs is the idea that they might be able to connect previous information to the present task, such as using previous video frames might inform the understanding of the present frame. If RNNs could do this, they’d be extremely useful. But can they? It depends.

In the text “I grew up in France… I speak fluent French.” Recent information suggests that the next word is probably the name of a language, but if we want to narrow down which language, we need the context of France, from further back. It’s entirely possible for the gap between the relevant information and the point where it is needed to become very large.

Thankfully, LSTMs can handle long-term dependencies.

**Unfortunately, as that gap grows, RNNs become unable to learn to connect the information.**

## LSTM Networks (Aka Long Short Term Memory Networks)

Long Short Term Memory networks – usually just called “LSTMs” – are a special kind of RNN, capable of learning long-term dependencies. They work tremendously well on a large variety of problems, and are now widely used. LSTMs are explicitly designed to avoid the long-term dependency problem. Remembering information for long periods of time is practically their default behavior.

All recurrent neural networks have the form of a chain of repeating modules of neural network. In standard RNNs, this repeating module will have a very simple structure, such as a single tanh layer.

![alt tag](http://colah.github.io/posts/2015-08-Understanding-LSTMs/img/LSTM3-SimpleRNN.png)

The figure above shows the repeating module for a standard RNN with a single tanh layer.

LSTMs also have this chain like structure, but the repeating module has a different structure. Instead of having a single neural network layer, there are four, interacting in a very special way.

![alt tag](http://colah.github.io/posts/2015-08-Understanding-LSTMs/img/LSTM3-chain.png)

From the figure above, the repeating module in an LSTM contains four interacting layers.

![alt tag](http://colah.github.io/posts/2015-08-Understanding-LSTMs/img/LSTM2-notation.png)

## Core Idea Behind LSTMs

The key to LSTMs is the cell state, the horizontal line running through the top of the diagram.

The cell state is kind of like a conveyor belt. It runs straight down the entire chain, with only some minor linear interactions. It’s very easy for information to just flow along it unchanged.

![alt tag](http://colah.github.io/posts/2015-08-Understanding-LSTMs/img/LSTM3-C-line.png)

