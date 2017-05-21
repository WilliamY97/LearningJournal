## Missing the Interaction

Without actions, the apps would just navigate and display products and order, but orders cannot yet be created.

## Creating a New Order Record

To manage a new order's information, we need an empty order record to work with.

in app/services/store.js

```
newOrder() {
  return Order.create({
    items: products.map((product) => {
      return LineItem.create({
        product: product
      });
    })
  });
}
```
## Using the New Order Record

The orders.index route is created and uses the new order record

## Introducing Actions

Actions map generic DOM events to specific application activities and functions.

Ex. Clicking read more link expands an article

## Intercepting the Submit Event from a form

Mapping an action: actions are mapped in templates using the {{action}} helper, defined on the element to watch.

```
{{action "actionName" on="eventName"}}
```

You add this to the form ```<form {{action "actionName" model on="eventName"}}>```

**actionName** fires off the "createOrder" action
Any extra parameters are passed to the triggered action as parameters
The action tirggers when the form emits a **eventName** event.
Passes in model as parameter

## Handling Actions
Action handlers are functions defined in an "actions" block on the route or its parents

app/routes/orders/index.js

```
  actions: {
    createOrder(order) {
      const name = order.get('name')
      alert(name + ' order saved!');
      }
    },
```

1. The new order record populates the template as the model
2. The triggered action passes the new order record to the action

## Transitioning to a New Route

Routes have a ```transitionTo``` function used to navigate to other routes.

```
  createOrder(order) {
    this.get('store').saveOrder(order);
    this.transitionTo('orders.order', order);
    }
```

## Saving the Order in the Store

Here, new orders are saved by giving them an ID and adding them to the orders collection.

app/services/store.js

```
saveOrder(order) {
  order.set('id', 9999);
  orders.pushObject(order);
}
```
pushObject comes from Ember, it's like push, but triggers value changed events.

## Ordering In Bulk

To finish the order form, the design calls for a button to increment item quantities by 10

```<button {{action "addToItemQuantity" item 10}}>+10</button>```

- Hand it the item and icrement amount.
- This {{action}} is using the default ```on="click"``` trigger
- Passing two arguments to the action to make this action more reusable: the item and the amount to increment

## Incrementing Property Values

Ember.Object provides incrementProperty and decrementProperty to quickly change numerics

Now once again gotta go back to app/routes/orders/index.js and add 

```
  actions: {
    addToItemQuantity(lineItem, amount) {
      lineItem.incrementProperty('quantity', amount);
      },
      createOrder(order)
  },
```

## Adding input helpers

```{{input value=option.value class="form-input" type="text"}}```

These would exist in forms to be values submitted upon an action.
