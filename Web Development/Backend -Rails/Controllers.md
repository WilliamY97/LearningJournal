# Controllers

You shouldn't call the record model in the view. This should occur in the controller.

When a request is made to for example /tweets/1 - the request goes through a controller in /app/controllers/tweets_controller.rb

Folder for views, controller, and URL all have the word tweets in it.

### /app/controllers/tweets_controller.rb

```
class TweetsController < ApplicationController
  def show
    @tweet = Tweet.find(1)
  end
end
```

```
<h1><%= @tweet.status %></h1>
```

No coincidence that method for show is the same as view show.html.erb. We can move tweet record find into method.

Variable Scope? How does view have access to variables? The answer is that we need it to be an instance variable @var

### How about having the show method map to another view?

show -> status.html.erb

Simply render the action in the show method. 

```
class TweetsController < ApplicationController
  def show
    @tweet = Tweet.find(1)
    render action: 'status'
  end
end
```

### Parameters akaa Params

Rails generates a hash called params when enter a controller method that takes values from the URL and provides them as key/value pairs.

```
class TweetsController < ApplicationController
  def show
    @tweet = Tweet.find(params[:id])
    render action: 'status'
  end
end
```

Often in Rails however the values passed in from URL are a hash of a hash.

We can deal with this by doing -> @tweet = Tweet.create(status: params[:tweet][:status])

Alternate Syntax @tweet = Tweet.create(params[:tweet])

Dangerous because user might be able to set any attributes. In Rails 4 we require strong parameters.

```Tweet.create(params.require(:tweet).permit(:status))```

If there were multiple things we needed to permit. We could use an array:

```Tweet.create(params.require(:tweet).permit([:status, :location])```

## Responding with XML or JSON

/tweets/1.json
/tweets/1.xml

```
class TweetsController < ApplicationController
  def show
    @tweet = Tweet.find(params[:id])
    respond_to do |format|
      format.html # show.html.erb by default
      format.json { render json: @tweet }
      format.xml {render xml: @tweet }
  end
end
```

## Authentication

```
class TweetsController < ApplicationController
  def show
    @tweet = Tweet.find(params[:id])
    if session[:zombie_id] != @tweet.zombie_id
      flash[:notice] = "Sorry, you can't edit this tweet"
      redirect_to(tweets_path)
    end
end
```

**Session:** Works like a per user hash
**flash[:notice]:** To send messgaes to the user

We re-direct to tweets_path because we don't want to route to a successful show. Instead we can redirect the request.

Alternative Syntax: ```redirect_to(tweets_path, notice: "Sorry, you can't edit this!")```

In the /app/views/layouts/application.html.erb we need to tell it where this notice message will show up.

```
<% if flash[:notice] %>
  <div id="notice"><%= flash[:notice] %> </div>
<% end %>
```

## Controller Actions

Edit, update, and destroy all need authorization. This isn't dry if we repeat it. Instead we add them into helper methods and use
before_action to initialize a callback function on the CRUD operations.

```
  before_action :get_tweet, only: [:edit, :update, :destroy]
  before_action :check_auth, only: => [:edit, :update, :destroy]
  def get_tweet
    @tweet = Tweet.find(params[:id])
  end
  
  def check_auth
    if session[:zombie_id] != @tweet.zombie_id
      flash[:notice] = "Sorry, you can't edit this tweet"
      redirect_to(tweets_path)
    end    
  end
```

