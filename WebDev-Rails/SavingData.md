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

##Part 1: Model

```
rails generate model Message
```

Command creates a new model. In doing so, Rails created two files:

- Model file in app/models/message.rb
- Migration file in db/migrate **migration files are a way to update the database**

**Migration File**

- Change method tells Rails what change to make to the database. It uses create_table method to create a new
table in the database for storing messages.

- Inside create_table, we added t.text :content. This will create a text column called content in the model tables
- t.timestamps creates two columns **created_at** and **updated_at**. They automatically set when a message is created
and updated.

```rake db:migrate``` updates the database with the new data model

```rake db:seed``` commands seeds the database with sample data from db/seeds.rb

##Part 2: Controller Action

```
def index
  @messages = Message.all
end
```

This method is added to the messages_controller so that routing to index will retrieve all messages from database and store them in variable @messages.

Rails has seven standard controller actions that can be used to do common things like display and modify data.

![Reference Image](https://s3.amazonaws.com/codecademy-content/projects/3/seven-actions.svg)

Use ```resources :messages``` to make routes for all seven actions in app.

If only for specific actions we can use :only to fine tune the resource route. ```reseources :messsages, only: [:index, :show]'''

##Part 3: Controller Action

```
<% @messages.each do |message| %> 
<div class="message"> 
  <p class="content"><%= message.content %></p> 
  <p class="time"><%= message.created_at %></p> 
</div> 
<% end %>
```

Putting this under the index.html.erb file under the views/messages to make the design and display of the message index route.

This file is known as a **web template**. Web templates are HTML files that contain variables and control flow statements. We use them to display data from the database.

##Creating a new/create action

```
def new
  @message = Message.new
end
```
A new method in the Messages controller and

```
post 'messages' => 'messages#create'
```
in routes
