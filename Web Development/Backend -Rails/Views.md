# Views

The visual representation of the application.

app/views/we-can-create-folders-here-for-model-views

.ERB -> Stands for embedded ruby.

### /app/views/tweets/show.html.erb

```
<!DOCTYPE html>
<html>
  <head><title>RailsForZombies</title></head>
  <body>
    <header>...</header>
    
    <% tweet = Tweet.find(1) %>
    <h1><%= tweet.status %></h1>
    
  </body>
</html>
```
<% ... %> -> Evaluates to Ruby Code
<%= ... %> -> Evalutaes Ruby and Prints the results

## Templating

We don't want to keep repeating this header code which is not D.R.Y. (Don't
repeat yourself) so instead we will seperate it into templates.

### /app/views/layouts/applications.html.erb

```
<!DOCTYPE html>
<html>
  <head><title>RailsForZombies</title></head>
  <body>
    <header>...</header>
    <%= yield %>
  </body>
</html>
```

The ```<%= yield %>``` command tells where the contents of page go.

### /app/views/tweets/show.html.erb

```  
<% tweet = Tweet.find(1) %>
<h1><%= tweet.status %></h1>
<p>Posted by <%= tweet.zombie.name %></p>
```

### Generating Links

```<%= link_to tweet.zombie.name, zombie_path(tweet.zombie) %>```

Shortcut: ```<%= link_to text_to_show, model_instance %>```

We should never need to hard code links - Rails provides link methods.
