# Organizing the Data

The same data structures are being used across the app and should be centralized.

# Generating a Service

Services are long-living objects (aka, "singletons") that are available throughout your app.

Services are good for: centralized logging, user sessions, websocket management, data repositories.

Create an ember service by ```ember generate service <service-name>```

