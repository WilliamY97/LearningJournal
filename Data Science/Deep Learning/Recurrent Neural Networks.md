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

The LSTM does have the ability to remove or add information to the cell state, carefully regulated by structures called gates.

Gates are a way to optionally let information through. They are composed out of a sigmoid neural net layer and a pointwise multiplication operation.

![alt tag](http://colah.github.io/posts/2015-08-Understanding-LSTMs/img/LSTM3-gate.png)

The sigmoid layer outputs numbers between zero and one, describing how much of each component should be let through. A value of zero means “let nothing through,” while a value of one means “let everything through!”

An LSTM has three of these gates, to protect and control the cell state.

## Step-by-Step LSTM Walk Through

### Forget Gate Layer

The first step in our LSTM is to decide what information we’re going to throw away from the cell state. This decision is made by a sigmoid layer called the “forget gate layer.”

It looks at ht−1 and xt, and outputs a number between 0 and 1 for each number in the cell state Ct−1. A 1 represents “completely keep this” while a 0 represents “completely get rid of this.”

Example. Let’s go back to our example of a language model trying to predict the next word based on all the previous ones. In such a problem, the cell state might include the gender of the present subject, so that the correct pronouns can be used. When we see a new subject, we want to forget the gender of the old subject.

![alt tag](http://colah.github.io/posts/2015-08-Understanding-LSTMs/img/LSTM3-focus-f.png)

### Input Gate Layer

The next step is to decide what new information we’re going to store in the cell state. This has two parts. First, a sigmoid layer called the “input gate layer” decides which values we’ll update. Next, a tanh layer creates a vector of new candidate values, ~Ct, that could be added to the state. In the next step, we’ll combine these two to create an update to the state.

Then we go ahead and update the old cell state, Ct-1, into the new cell state Ct. The previous steps already decided
what to do, we just need to actually do it.

We multiply the old state by ft, forgetting the things we decided to forget earlier. Then we add it * ~Ct. This is the
new candidate values, scaled by how much we decided to update each state value.

Finally, we need to decide what we’re going to output. This output will be based on our cell state, but will be a filtered version. First, we run a sigmoid layer which decides what parts of the cell state we’re going to output. Then, we put the cell state through tanhtanh (to push the values to be between −1−1 and 11) and multiply it by the output of the sigmoid gate, so that we only output the parts we decided to.
