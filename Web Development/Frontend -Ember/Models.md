# Introducing Models

Models represent the underlying (and sometimes persisted) data of the application.

They are contained in app/models/example.js

## Extending from Ember.Object
Ember.Object provides:
1. Consistent interface for creating and destroying records
2. Object lifecycle events and hooks
3. Properties and property observation functionality

This is how templates are updated when properties change.

## Interacting With Models

Properties are read and set using get() and set()

```
export default Ember.Object.extend({});
```

Ember.Object provides create(). Record properties may optionally be passed in at creation.

## Using the Ember.Object Models

With basic models defined, we can use them them in the store service.

```import example from 'woodland/models/example-item';``` -> service/store.js
