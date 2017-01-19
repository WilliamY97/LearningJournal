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
