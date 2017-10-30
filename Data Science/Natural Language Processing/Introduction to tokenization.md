# What is tokenization?

- Turning a string or document into tokens (smaller chunks)
- One step in preparing a text for NLP
- Some examples:
  - Breaking out words or sentences
  - Separating punctuation
  - Separating all hashtags in a tweet

Oftem ```nltk``` or the natural language toolkit is used for this.

```
In [1]: from nltk.tokenize import word_tokenize

In [2]: word_tokenize("Hi there!") 
Out[2]: ['Hi', 'there', '!']
```

# Why Tokenize?

- Easier to map part of speech
- Matching common words
- Removing unwanted tokens

Ex. "I don't like Sam's shoes."
"I", "do", "n't", "like", "Sam", "'s", "shoes", "."

# Other nltk tokenizers

```sent_tokenize:``` tokenize a document into sentences

```regexp_tokenize:``` tokenize a string or document based on a regular expression pattern

```TweetTokenizer:``` special class just for tweet tokenization, allowing you to separate hashtags, mentions and lots of exclamation points!!!

