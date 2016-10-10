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
