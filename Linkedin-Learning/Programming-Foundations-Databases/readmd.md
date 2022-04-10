## Programming Foundations Databases

### Introduction

#### Understanding database: Benefits of structured data
* Provide structure for data
* Allow enforcement of rules for data
* Protect data from unauthorized access or changes

#### Normalization Rules:
are considered to be the standard level of optimization for a business database (helps us prevent problems in working with our data, and the process should be revisited whenever there's a change to the schema or the structure of a database)

#### First Normal Form (1NF)
__values in each cell should be atomic and tables should have no repeating groups__
This means that each field in each table __has only one value in each cell__ and that there are no columns representing repeated kinds of data for each row
First Normal form is often extended to include the idea that there aren't duplicate rows in a table
This also suggests that the order of rows and columns is not importnat to the data

#### Second Normal Form (2NF)
__No value in a table should depend on only part of a key that can be used to uniquely identify a row__
This means that for every column in the table that isn't a key, each of the values must rely on only the whole key
the values must describe something about that row that we can't determine from just the part of a key
this problem comes up in the context of composite keys

#### Third Normal Form (3NF) (is the best practice)
__Values should not be stored if they can be calculated from another non-key field__
* low duplication
* high integrity
* durable when you create CRUD

#### Denormaliztion
__The process of intentionally duplicating information in a table, in violation of normalization rules__
* Denormalization is done to a previously normalized database
it doesn't mean skipping normalization altogether
* Denormalization is a trade-off. Gaining speed way may reduce consistency
and that's a decision you'll need to make based on your own business requirements

------------------------

#### Aggregate Functions
which use more than one piece of data to generate a value