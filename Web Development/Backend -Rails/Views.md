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

## Generating Links

```<%= link_to tweet.zombie.name, zombie_path(tweet.zombie) %>```

zombie_path in this case just re-routes to show.html with new zombie

Shortcut: ```<%= link_to text_to_show, model_instance %>```

We should never need to hard code links - Rails provides link methods.

### Options with link_to

```<%= link_to tweet.zombie.name, 
   zombie_path(tweet.zombie),
   confirm: "Are you sure?%>```
   
## index.html.erb

```
<h1>Listing Tweets</h1>
<table>
  <tr>
    <th>Status</th>
    <th>Zombie</th>
  </tr>
<% tweets = Tweet.all %>
<% tweets.each do |tweet| %>
  <tr>
    <td><%= link_to tweet.status, tweet %></td>
    <td><%= link_to tweet.zombie.name, tweet.zombie %></td>
    <td><%= link_to "Edit", edit_tweet_path(tweet) %></td>
    <td><%= link_to "Destroy", tweet, method: :delete %></td>
  </tr>
<% end %>
<% if tweets.size == 0 %>
 <em>No Tweets Found</em>
<% end %>
</table>
```
### Design: What happens if no tweets to display?

Store the tweets in a variable and check if there is anything in it with an if
statement afterwards to see if there isn't anything in it. Then print an error
message.

## URL Generator Methods

Action -> Code -> The URL

List all tweets -> tweets_path -> /tweets

New tweet form -> new_tweet_path -> /tweets/new

These url generators above require a tweet(record) as an argument

Action -> Code -> The URL
Show a tweet -> tweet_path -> /tweets/1

Edit a tweet -> edit_tweet_path(tweet) -> /tweets/1/edit

Delete a tweet -> tweet, method: :delete -> /tweets/1




