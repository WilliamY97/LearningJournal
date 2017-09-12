# Knuth–Morris–Pratt Algorithm

Resource: https://www.youtube.com/watch?v=GTJr8OvyEVQ

KMP is an algorithm used for substring searching. It allows for someone to identify a specific string pattern in a text.

## Algorithm Steps
We start from the zero'th index of the text and pattern. If there is no match then we move to the next letter of the text. Then
we compare if the letters match - if they do then we compare the next letter of both the text and pattern. We keep doing this
if they match until the end of pattern. If they don't match then we must iterate to the next letter of the text and start the
process over again.

