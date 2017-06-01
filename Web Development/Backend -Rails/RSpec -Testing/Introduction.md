# Introduction

- Popular Ruby testing framework
- Less Ruby-like, natural syntax
- Domain Specific Language for testing - Added additional language features on top of Ruby
- Well-formatted output

RSpec evolved from Behaviour Driven Development

## Installing RSpec

1. ```gem install respec```
2. rspec --init (Initialize two files spec_helper and rspec)

We will be building an object in /lib/object.rb

In Rspec we substitute test with specification.

We put our specifications in the /spec/ directory

### ```spec/lib/zombie_spec.rb``` <- where tests aka specs go

```
  require "spec_helper"
  require "zombie" # requires zombie class
  
  describe Zombie do
    it "is named Ash"
      zombie = Zombie.new
      zombie.name.should == 'Ash'
    end
    
    it "has no brains" do
      zombie = Zombie.new
      zombie.brains.should < 1 #modifier < matcher
    end
  end
```

Calling ```rspec spec/lib/zombie_spec.rb``` runs tests - in this case it would fail
but if the lib/zombie.rb file were to be updated to have a :name then it would pass

An assertion would be called an expectation in RSpec


