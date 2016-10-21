#Database Design

These are steps to help design both small and large databases.

##Step 1: Handle Ambiguity

- Before you proceed with your design, you must understand exactly what you need to design.

- Ex. Design system for apartment rental agency. You will need to know whether this agency has multiple locations or just one. Should the person be able to rent out two apartments in the same building? **Some very rare conditions might be best handled through a work around (like duplicating the person's contact information in the database)**

##Step 2: Define the Core Objects

- Now we should look at core objects of our system. Each of these core objects typically translates into a table. In the case above, this would be: **Property, Building, Apartment, Tenant, and Manager**

##Step 3: Analyze Relationships

- Outlining the core objects should give us a good sense of what the tables should be. The important question is how do these tables
relate to each other? Are they **many-to-many** or **one-to-many**

Ex. Buildings has a one-to-many relationship with Apartments (one Building has many Apartments)

- This would be achieved by linking the Apartments table back to Buildings with a BuildingID column.

Ex. If we want to allow for the possibility that one person rents more than one apartment, we might want to implement a many-to-many relationship as follows:

If we want to allow for the possibility that one person rents more than one apartment, we might want to implement a many-to-many relationship as follows:?

- This would be achieved by creating a new table called **TenantApartments** that stores relationship between Tenants and Apartments by holding the TenantID and ApartmentID.

