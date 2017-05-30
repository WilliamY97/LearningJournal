# Active Record Queries

Active Record is the M in MVC - the model - which is the layer of the system responsible for representing business data and logic.
Active Record facilitates the creation and use of business objects whose data requires persistent storage to a database. It is an
implementation of the Active Record pattern which itself is a description of an Object Relational Mapping system.

## CRUD Operation Examples

### READ
```
Tweet.find(3)
```

### CREATE
```
t = Tweet.new
t.status = "Hello world!"
t.save
```

Alternate Syntax:
You can pass in all the attributes you want to create with record

```
t = Tweet.new(
  status: "Hello World!",
  zombie: "Jim")
t.save
```

Alternate Syntax 2:
Immediate creation of record with attributes passed in (No Save necessary)

```
Tweet.create(status: "Hello World!",
  zombie: "Jim")
```

### UPDATE
```
t = Tweet.find(3)
t.zombie = "EyeballChomper"
t.save
```

### DELETE
```
t = Tweet.find(3)
t.destroy
```


