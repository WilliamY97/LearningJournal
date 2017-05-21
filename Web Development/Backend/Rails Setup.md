#Setup

- Setting up new application for Rails

```
rails new
```

Creates a new Rails app named MySite. It generated a number of files and folders that we will use to build the app.

```
bundle install
```

Installed all the software packages needed by the new Rails app. These software packages are called **gems** and 
they are listed in the file **Gemfile**.

```
rails server
```

Started the Rails development server so that we could preview the app in the browser by visiting http://localhost:8000.
This development server is called WEBrick.

##Request / Response Cycle

**What Happens When You Visit http://localhost:8000 in the Browser?**

1. The browser makes a request for the URL http://localhost:8000.

2. The request hits the Rails router in config/routes.rb. The router recognizes the URL and sends the request to 
the controller.

3. The controller receives the request and processes it.

4. The controller passes the request to the view.

5. The view renders the page as HTML.

6. The controller sends the HTML back to the browser for you to see.

---

```
rails generate controller Pages
```

Generated a new controller named Pages. This created a file named **app/controllers/pages_controller.rb**

```
class PagesController < ApplicationController
  
  def home
  end
  
  
end
```
- Inside the new Pages controller, we add a method called home. Methods in rails controllers are also referred to as
**controller actions**, so here we add the **home** action to the pages controller

##Creating Routes

Moving on to the second part of the request/response cycle and create a route.

In **config/routes.db** we add:

```
Rails.application.routes.draw do
  get 'welcome' => 'pages#home'
```

Now when a user visits http://localhost:8000/welcome, the route will send a request to the Page's controller's **home** action

Once we have a controller and a route, we can do the third part of the request/response cycle and create a **view.**

In **app/views/pages/home.html.erb** we can add the view for the route we made to #home that leads to home.html.erb

```
<div class="main">
  <div class="container">
    <h1>Hello my name is __</h1>
    <p>I make Rails apps.</p>
  </div>
</div>
```

##Generalizing the Setup Process

1. Generate a new Rails app.
2. Generate a controller and add an action.
3. Create a route that maps a URL to the controller action.
4. Create a view with HTML and CSS.
5. Run the local web server and preview the app in the browser.
