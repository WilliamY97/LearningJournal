# Templating

A template is what tells Ember to render as HTML and display in the web browser

app > templates > application.hbs (hbs is handlebars)

By convention, all Ember applications use an application template

## Changing the Heading

Curly brace {{outlet}} is a handlebar expression marking locations of logic or dynamic content

Outlet is an expression that acts as a placeholder. Allows us to inject other templates into current page.

Ember generates sane defaults across the application automatically -> often empty.

## Customizing the Index Template

We can create more templates like index.hbs which shows by default for '/'. The system will not always have a default
for all templates.

## Router

Manages application's state. Keeps track of what someone is doing and maps it to the path of the URL.

In app > router.js there is a router.map section. We should configure this like so:

```this.route('orders', {path: '/orders' });```

Ember already does this for index.hbs under the hood

If the name of the endpoint matches the name, we can omit the path -> 
```this.route('orders');```

## Navigating Between Endpoints

Don't use anchor tags because it full-page refreshes the page. Instead we can use the link-to helper.

```{{#link-to "orders"}}Orders{{/link-to}}```

This is using a block form similar to Ruby blocks. Ember now knows clicks and intercepts them for this tag
and handles them on the client-side which is much faster.

We can also add classes into the tag like so

```{{#link-to "orders" class="orders-link" tagName='div'}}Orders{{/link-to}}```

Tag name can change it into a div object or something else instead of an anchor tag

## Questions 

**What is the name of the outermost template that is available in all Ember applications?**

Application Template

**Where the application template is located?**

app/templates/application.hbs
