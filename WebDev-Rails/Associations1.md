#Associations 1 

In the model files, we used the methods **has_many** and **belongs_to** define an association between models.

has_many :destinations denotes that a single Tag can have multiple Destinations.

belongs_to :tag denotes that each Destination belongs to a single Tag.

The has_many and belongs_to pair is used to define one-to-many relationships. A few are:

- a Library has many Books; a Book belongs to a Library

- an Album has many Photos; a Photo belongs to an Album

- a Store has many Products; a Product belongs to a Store
