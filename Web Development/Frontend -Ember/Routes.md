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

Dynamic segments are a part of the URL path that holds variable data, like identifiers.

## Using the Dynamic Segment Values

The router passes the dynamic segement values to the route's model hook.

We can add a params to the model hook so that it can take the hash with the id in it.

```model(params) {
return [ 
{id:'1', name: 'Nate'} 
].findBy('id', params.order_id);
} 
});
```

## Linking to a Single Item

So now we can add to the link-to helper which accepts one or more objects to populate the dynamic segments.

```
{{#each model as |order|}}
  {{#link-to "order" order}}
    Order {{order.id}} for {{order.name}}<br>
  {{/link-to}}
{{/each}}
```

This links to the "order" route and passes the order that we'd like to view.

**The {{link-to}} helper automatically uses the given object's ID as the dynamic segment value**

## Visualizing the Current Structure

Everything currently just gets rendered into the {{outlet}} in application.hbs

## Nesting the Order Routes

```
Router.map(function() {
  this.route('orders', function() {
    this.route('order', { path: '/:order_id' }):
  });
});
```

A nested mapping allows multiple routes and templates to be displayed

A new "orders.index" route is automatically created.

Index routes are always created for parent routes. They're what's rendered when you go to the parent.

## Fixing Broken Links

Nesting indtroduced the "orders" route namespace. Links need to get updated to match.

orders -> orders.order. Also orders.hbs needs an {{outlet}} now too.

## Relocating Nested Files

Nesting introduced an "orders/" directory namespace. Files must move to match.

