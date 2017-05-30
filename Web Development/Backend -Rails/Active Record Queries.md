# Active Record Queries

Active Record is the M in MVC - the model - which is the layer of the system responsible for representing business data and logic.
Active Record facilitates the creation and use of business objects whose data requires persistent storage to a database. It is an
implementation of the Active Record pattern which itself is a description of an Object Relational Mapping system.

## CRUD Operation Examples

### READ
```
Tweet.find(3)
```

Multiple Parameters:

```
Tweet.find(3,4,5)
```

Specific Positions:

```
Tweet.first Tweet.last Tweet.all
```

Returns total number of records:

```
Tweet.count
```

Returns all records, ordered by attribute:
```
Tweet.order(:person)
```

Returns first 10 records
```
Tweet.limit(10)
```

Returns all tweets from person named 'ash'
```
Tweet.where(person: "ash")
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

Alternate Syntax:

```
t = Tweet.find(3)
t.attributes = { status: "Brains",
  zombie = "EyeballChomper" }
t.save
```

Update method:

```
t = Tweet.find(3)
t.update (status: "Brains",
  zombie = "EyeballChomper")
```

### DELETE
```
t = Tweet.find(3)
t.destroy
```

Destroy all records:

```
Tweet.destroy_all
```

## Method Chaining (Complex Queries)

We can chain queries to provide a large restriction

```
Tweet.where(person: "ash").order(:status).limit(10)
```


