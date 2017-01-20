#Object Oriented Programming I

Classes have the ability to create new Ruby objects of class NewClass. By convention, class names start with a capital
letter and use CamelCase instead of relying on underscores.

**Initialize** is the constructor for a class.

**Instance Variable** means that the variable is attached to the instance of the class. For example,

```
class Car
  def initialize(make, model)
    @make = make
    @model = model
  end
end

kitt = Car.new("Pontiac", "Trans Am")
```

Creating a new instance of a class:

```
me = Person.new("Eric")
```

##Scope

The scope of a variable is the context in which it's visible to the program.

**Global Variables:** Available everywhere - $

**Local Variables:** Available only in certain methods 

**Class Variables:** Available in certain classes - @@

**Instance variables:** Available to a particular instance - @

##Inheritance

Inheritance is the process by which one class takes on the attributes and methods of another, and it's used to express an is-a relationship. A fox **is a** animal.

```
class ApplicationError
  def display_error
    puts "Error! Error!"
  end
end

class SuperBadError < ApplicationError
end

err = SuperBadError.new
err.display_error
```

SuperBadError doesn't have the display_error method, but it inherits from ApplicationError and so it can call the method.

##Overriding

Sometimes we want one class that inherits from another to not only take on the methods and attributes of its parent, but to override one or more of them.

Writing a method with same name as a method you will inherit will **overrride** it and allow you to use the method you wrote instead.

##

##Multiple inheritance
