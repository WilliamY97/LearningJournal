# Routing

## Driving With Data

Ember has been automatically generating a hidden layer between the router and templates.

Routes are responsible for collecting data and rendering the proper templates.

Router -> Routes -> Templates

## Auto-generated Routes

Auto-generated routes render the template of the same name

## Generating a Route

Ember CLI provides a generator for creating a route and updating the router.

```ember generate route <route-name>```

This generates a route for us ```this.route('orders');``` and a template orders.hbs.

Also creates app/routes/orders.js

## Examining the Route

Routes are defined in app/routes with a file name matching their route name

## Customizing the Route's Model
The model hook returns the data used in the route and its template
```model() { return 'test' } });```

Now we can call {{model}} in the orders.hbs file to load from orders route

Having something like ```return { id: '1', name: 'Nate'};``` would allow us to call {{model.id}}

## Working with Collections

If we return a object with values like the one above in an array we can iterate through it.

The {{#each}} helper iterates over a collection and renders the block once for each item.

```
{{#each model as |order|}}
  Order {{order.id}} for {{order.name}}<br>
{{/each}}
```

## Linking to a Single Item

Now that we're displaying orders, we still need to link each one.

```
{{#each model as |order|}}
  {{#link-to ???}}
    Order {{order.id}} for {{order.name}}<br>
  {{/link-to}}
{{/each}}
```

In order to link to a single item, we need a route that can load and render a single item.

## Defining Dynamic Segments in the Router

Add to the router.js ```this.route('order', { path: '/orders/:order_id' });```
