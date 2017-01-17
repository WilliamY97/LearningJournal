#Saving Data

For a basic rails application, we need to use a controller, route, and view. The **request/response cycle** is a useful
guide to see how all the app's files and folders fit together.

##Request/Response Cycle

![Reference Image](https://s3.amazonaws.com/codecademy-content/projects/3/request-response-cycle-static.svg)

1. User opens up browser and types in URL
2. When they press enter it makes request for URL
3. Request hits route and router maps URL to controller/action
4. Action receives request and passes it on to the view
5. View renders in HTML
6. Controller sends the HTML back to browser. Page loads and the user sees it.

