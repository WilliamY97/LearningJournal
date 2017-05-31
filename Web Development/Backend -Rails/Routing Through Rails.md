# Routing Through Rails

In order to propery find the paths and route them to actions. We need to define routes inside of our router.

```
ZombieTwitter::Application.routes.draw do
  resources :tweets
  get '/new_tweet' => 'tweets#new'
  get '/all' => 'tweets#index', as: 'all_tweets'
  get '/all' => redirect('/tweets')
  root to: "tweets#index"
end
```

## Routes

Code -> The URL -> TweetsController

tweets_path -> /tweets -> def index

tweet -> /tweet/<id> -> def show

new_tweet_path -> /tweets/new -> def new

edit_tweet_path(tweet) -> /tweets/<id>/edit -> def edit

## Custom Paths

We can create a link using the custom path by doing:
```
<%= link_to "All Tweets", all_tweets_path %>
```
It will properly link to the all url

## Root Route

```<%= link_to "All Tweets", root_path %>```
What users go to as the first domain.

## Route Parameters

get '/local_tweets/:zipcode' => 'tweets#index' as 'local_tweets'

then in the index method just write logic that deals with zipcode key value pair.

the as ... allows us to do <%= link_to "Tweets in 32828", local_tweets_path(32828) %>

get ':name" => 'tweets#index', as: 'zombie_tweets'
<%= link_to "Gregg", zombie_tweets_path('greggpollack') %>

then in the index method check if there is a params[:name] and implement logic for it
