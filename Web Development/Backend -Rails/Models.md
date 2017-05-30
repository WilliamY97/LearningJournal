# Models

How the Rails application communicates with the datastore.

### app/models/tweet.rb
```
class Tweet < ActiveRecord::Base
  validates_presence_of :status
  validates_numericality_of :fingers
  validates_uniqueness_of :toothmarks
  validates_confirmation_of :password
  validates_acceptance_of :zombification
  validates_length_of :password, minimum: 3
  validates_format_of :email, with: /regex/i
  validates_inclusion_of :age, in: 21..99
  validates_exclusion_of :age, in: 0...21, message: "Sorry you must be over 21"
end
```

ActiveRecord::Base maps the class to the table

**t.errors.messages** - Checks what errors have occured in the record object

## Record Validations

Rails comes with multiple validations for model classes that can be added in order to require something before
the model object can be created.

**validates_presence_of** - Checks if new records has the status attribute or else doesn't save

**validates_numericality_of** - Makes sure something is a number

**validates_uniqueness_of** - Makes sure somethign is unique

**validates_confirmation_of** - Makes sure two fields equal before saving

**validates_acceptance_of** - Checkbox that may need to check

**validates_length_of** - Check if something is long enough

**validates_format_of** - Express a regex that needs to be met

**validates_inclusion_of** - Makes sure a field is between two values

**validates_exclusion_of** - Makes sure something is not included from between two values

