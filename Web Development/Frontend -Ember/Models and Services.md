# Organizing the Data

The same data structures are being used across the app and should be centralized.

# Generating a Service

Services are long-living objects (aka, "singletons") that are available throughout your app.

Services are good for: centralized logging, user sessions, websocket management, data repositories.

Create an ember service by ```ember generate service <service-name>```

With a service in place, the share data can be moved from the routes into a function in services.

```
export default Ember.service.extend({
    getOrders() {
      return [
        { id: '1', name: 'Nate' },
        { id: '2', name: 'Gregg' }
    }
  }
});
```

Service objects are made available within another object using Ember.inject.service()

```
export default Ember.Route.extend({
  model() {
    const store = this.get('store'); //grabs property store and assigns to variable
    return store.getOrders();
  },
  store: Ember.inject.service('store')
});
```

## Centralize the Data Filtering

Now that the data is in the service, the service can be used to find and filter the app data.

Write another service method ```getOrderbyId(id)```

```getOrderById(id) {
    const orders = this.getOrders();
    return orders.findBy('id', id);
}
```
