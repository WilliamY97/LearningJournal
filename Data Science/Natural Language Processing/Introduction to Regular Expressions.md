# Introduction to Regular Expressions

What exactly are regular expressions?

- Strings with a special syntax
- Allow us to match patterns in other strings
- Applications of regular expressions:
  - Find all web links in a document
  - Parse email addresses, remove/replace unwanted characters
  
  Example 1: Basic Matching 
  ```
  import re
  re.match('abc','abcdef')
  OUTPUT: <_sre.SRE_MATCH object; space=(0,3), match='abc'>
  ```
  
  Example 2: Matching First Word
  ```
  word_regex = '\w+'
  re.match(word_regex, 'hi there!')
  OUTPUT: <_sre.SRE_MATCH object; space=(0,2), match='hi'>
  ```
  
  ## A Few Common Patterns
  
| Pattern | Matches | Example |
| --- | --- | --- |
| \w+         |     word      |    'Magic'   |
| \d          | digit         | 9            |
| \s     | space              | ''           |
| *      | wildcard    | 'username74'        |
| + or * | greedy match | `aaaaaa`           |
