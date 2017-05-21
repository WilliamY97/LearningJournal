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
