##Elementary Data Structures

##Data Type

- The set of allowed values for a variable

##Data Structure

- Systematic way of organizing and accessing data

##Principle of Abstraction

- Focus on what not how when solving a problem

##Abstract Data Type

- Set of elements together with a well-defined set of operations on these elements

#Abstract Data Types (ADTs)

- Allow to break work into pieces that can be work on independently without compromising correctness

- Serve as specifications of requirements for the building blocks of solutions to algorithmic problems

- Encapsulate data structures and algorithms that implement them

- Provide a language to talk on a higher level of abstraction

#Dictionary

- An element has a key part and a data part

- Accessor -> set of dynamic operations that returns back value without modification of content

- Dictionary ADT - a dynamic set with methods: how long does it take for us to access specific data?

- How long does it take to add data? How long does it take to delete data?

- If you can define these 3 operations for 3 data structures we have a common basis to compare DS's

- If order matters we can go in more detail (find min value, max value, successor?, predecessor)?

- ex. Successor to 10 is the next larger value than 10

- ex. Predecessor - returns next smaller element to 10 

- Index, search, delete are mandatory analysis

ex. Google search is very powerful because it uses hash tables (search comes back very quickly)

#Data Storage for ADT

- Data storage can be classified as either:

- Contiguous storage or node-based storage

ex. contig: values are stored beside each other

ex. node: each node contains data

