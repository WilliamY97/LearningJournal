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

##Subclass Revision

Sometimes working with subclass you override a method or attribute defined in that class' base class (also called a parent or superclass).

You can directly access the attributes or methods of a superclass with Ruby's built-in super keyword.

When you call super from inside a method, that tells Ruby to look in the superclass of the current class and find a method with the same name as the one from which super is called. If it finds it, Ruby will use the superclass' version of the method.

##Multiple inheritance

Not allowed. However, there are instances where you want to incorporate data or behavior from several classes into a single class, and Ruby allows this through the use of mixins. 

#Object Oriented Programming II

#Need-to-know Basis

Ruby allows you to explicitly make some methods public and others private. Public methods allow for an interface with the rest of the program; they say, "Hey! Ask me if you need to know something about my class or its instances."

Private methods, on the other hand, are for your classes to do their own work undisturbed. They don't want anyone asking them anything, so they make themselves unreachable!
