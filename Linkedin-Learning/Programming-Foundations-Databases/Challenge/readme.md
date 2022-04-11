## Challenge

<details>
    <summary><strong>Introduction Quiz</strong></summary>
    <strong>When you move data from an unstructured form to a structured form, what benefit do you gain?</strong>
    <br>
    all of these answers
    <br>
    Simpy putting your data into an organized structure, like a spreadsheet or table, brings a lot of benefits.
    <br>
    <br>
    <strong>When you store data in a database, what is one advantage you get over a plain spreadsheet?</strong>
    <br>
    Rows of data can be associated with each other across tables.
    <br>
    While some spreadsheets can simulate this capability with lookup functions, the ability to create relationships between tables is a core function of relational databases.
    <br>
    <br>
    <strong>What is one advantage of using a spreadsheet to store data?</strong>
    <br>
    It can help you see gaps in the data.
    <br>
    When pieces of information are arranged in a consistent way, it becomes easier to see what information you have.
    <br>
    <br>
    <strong>The definition of how data in a database will be organized is called the _____.</strong>
    <br>
    schema
    <br>
    The database's schema includes the information about the layout of tables and other information about the database itself.
</details>

<details>
    <summary><strong>Database Foundation Quiz</strong></summary>
    <strong>A unique value _____.</strong>
    <br>
    occurs only once in a given column
    <br>
    Unique values are useful because they never appear twice. If a value appears more than once in a given column, it's not unique in that column.
    <br>
    <br>
    <strong>A relationship connects two pieces of data in different _____ in the same _____.</strong>
    <br>
    tables; database
    <br>
    Even though a relationship is concerned with individual rows, a relationship is defined as being between tables in the same database.
    <br>
    <br>
    <strong>Which is a good example of a candidate key?</strong>
    <br>
    an employee ID number
    <br>
    Any piece of data that uniquely represents a row is a candidate key, and if you have a value that occurs in the data naturally, that's a natural key.
    <br>
    <br>
    <strong>How many SQL clauses are in this query?</strong>

```
SELECT Width,Height FROM Shapes;
```
two
<br>
Each keyword, SELECT and FROM, defines a single clause.
    <br>
    <br>
    <strong>In a database, what is a relation?</strong>
    <br>
    a set of attributes (columns) that describe information about specific instances (rows) of an entity
    <br>
    You may also see the rows called "tuples."
    <br>
    <br>
    <strong>What is the name of a key that consists of different fields taken together to act as a unique identifier?</strong>
    <br>
    composite key
    <br>
    A composite key combines two or more fields to act as a unique identifier.
    <br>
    <br>
    <strong>Which ACID step requires that the database is updated when the transaction completes successfully?</strong>
    <br>
    durable
    <br>
    Durability requires that data changed by the transaction is written to the database.
    <br>
    <br>
    <strong>When is an associative table useful?</strong>
    <br>
    when records need to be related in a many-to-many relationship
    <br>
    An associative (or linking) table relates foreign keys from different tables to associate their records.
    <br>
    <br>
    <strong>In the ACID model, which term represents the fact that a transaction can't be divided into smaller parts?</strong>
    <br>
    atomic
    <br>
    Even though you now know atoms can be broken down into smaller parts, the term atomic means that something can't be broken down into smaller pieces. Here, atomicity means that the transaction behaves as one single action.
    <br>
    <br>
    <strong>What would you use a relationship to connect?</strong>
    <br>
    a customer with their favorite table in the restaurant
    <br>
    This would be a one-to-many relationship. For every one table, there could be many customers who prefer to sit at it. But one customer cannot have many favorite tables.
    <br>
    <br>
    <strong>SQL is _____.</strong>
    <br>
    the language you use to communicate with a database
    <br>
    Structured Query Language is the most common language interacting with relational databases.
    <br>
    <br>
    <strong>What does the term transaction mean?</strong>
    <br>
    all of the steps for an action must be completed
    <br>
    A transaction is a collection of steps that must all be completed in order for a change to be made to the database.
    <br>
    <br>
    <strong>In the acronym CRUD, what does "R" stand for?</strong>
    <br>
    read
    <br>
    The letters stand for create, read, update, and delete. Good job!
</details>

<details>
    <summary><strong>Tables Quiz</strong></summary>
    <strong>If you reference a key from Table A in Table B, what is that value in Table B?</strong>
    <br>
    a foreign key
    <br>
    Because it refers to a key in another table, in this context, the value is called a foreign key.
    <br>
    <br>
    <strong>In this table, which field is likely to be a good primary key?</strong>
    <br>
    <img src="https://media-exp1.licdn.com/dms/image/C560DAQGoz8_Q4fBOyA/img_1280_ani/0/1611959263435?e=2147483647&v=beta&t=CSEQ3Q3GOAU-ym9rH8Okx1mgWuZTlXBAeyZP6Ksz-Z0">
    <br>
    EmployeeID
    <br>
    Because each employee is given a different ID number, this value is likely to be unique. So it's a good primary key for this table. Each ID refers to only one employee record.
    <br>
    <br>
    <strong>What would be a good name for a table containing customer details and contact information?</strong>
    <br>
    Customers
    <br>
    This name is short, descriptive, and uses a pluralized name based on the type of records it contains.
    <br>
    <br>
    <strong>In a database where you keep track of records for a school, what tables should you expect to find?</strong>
    <br>
    Students, Classes, and Grades
    <br>
    Each of these tables holds a different kind of information, and because the tables can store more than one record, the table names are pluralized.
    <br>
    <br>
    <strong>When storing the text Mozambique in a column with a data type of VARCHAR(8), what would be saved in the database?</strong>
    <br>
    Mozambiq
    <br>
    This data type can hold at most eight characters, so the remaining two are not stored.
    <br>
    <br>
    <strong>When talking about data types, what do you call the group of types that represent text?</strong>
    <br>
    string types
    <br>
    There are various kinds of string types to accommodate text of different lengths.
    <br>
    <br>
    <strong>To store the value 4:32PM, December 27, 2019, which data type would you use?</strong>
    <br>
    DATETIME
    <br>
    This is the correct type, because it includes both a date component and a time component. The other options here do not.
    <br>
    <br>
    <strong>Which condition represents a NULL value?</strong>
    <br>
    a date cell containing no data
    <br>
    A cell, regardless of its data type, is NULL when it has no value.
    <br>
    <br>
    <strong>Which table name follows best practice?</strong>
    <br>
    CheckDeposits
    <br>
    This table name correctly uses camel case and a plural form.
    <br>
    <br>
    <strong>If you don't use a number type to store numeric data, _____.</strong>
    <br>
    you need to take additional steps to process the data as a number whenever you use it
    <br>
    Storing numeric data in numeric data types gives you the ability to work with numbers directly, as you might do when you use mathematical operations in queries.
    <br>
    <br>
    <strong>Before you create a database, what do you need to know?</strong>
    <br>
    all of these answers
    <br>
    You can't create your database without knowing the basics of the tables, their columns, and how data will be related.
    <br>
    <br>
    <strong>Which statement is true regarding composite keys?</strong>
    <br>
    A composite key is likely useful when there is no primary key.
    <br>
    When a primary key does not exist, a composite key can be used to uniquely identify and relate a record to other data.
    <br>
    <br>
    <strong>When planning a database, what do you start with?</strong>
    <br>
    an Entity Relationship (ER) diagram
    <br>
    Using an ER diagram, you can plan out what fields will appear on which tables, and how they're related.
</details>

<details>
    <summary><strong>Relationships Quiz</strong></summary>
    <strong>Which is an example of referential integrity?</strong>
    <br>
    preventing the user from entering a record that refers to nonexistent data
    <br>
    If a field in one table refers to a column in another table, you can require that the value you reference exists in that other table before the database will allow you to enter a new record.
    <br>
    <br>
    <strong>Defining relationships helps you to do what?</strong>
    <br>
    all of these answers
    <br>
    Thinking about relationships between tables can bring you all of these benefits.
    <br>
    <br>
    <strong>What is it called if you delete a record and the database goes on and deletes other records associated with that record?</strong>
    <br>
    a cascading delete
    <br>
    If configured to do so, a delete operation can cascade across records linked with a relationship.
    <br>
    <br>
    <strong>A database must include one or more relationship.</strong>
    <br>
    FALSE
    <br>
    You can use tables in a database without defining any relationships.
    <br>
    <br>
    <strong>In a one-to-many relationship, the value representing the 'many' side is what?</strong>
    <br>
    foreign key
    <br>
    The foreign key points to the primary key for the 'one' side of the relationship.
    <br>
    <br>
    <strong>When modeling a many-to-many relationship, how should you name the linking table?</strong>
    <br>
    with a combination of the names of the tables it's linking
    <br>
    While it's not enforced by the DBMS, using tables named like this helps to keep queries readable and remind you what tables are for.
    <br>
    <br>
    <strong>When you need to create a many-to-many relationship, what do you need to generate?</strong>
    <br>
    a linking table that has a one-to-many relationship with two or more tables
    <br>
    By creating a linking table, you can associate many records with many others.
    <br>
    <br>
    <strong>Which scenario represents a one-to-many relationship?</strong>
    <br>
    bank customers linked to their bank accounts
    <br>
    A certain customer can have multiple accounts, but a certain account can belong to only one customer.
    <br>
    <br>
    <strong>A one-to-one relationship _____.</strong>
    <br>
    allows only one record to be connected to only one other record
    <br>
    A one-to-one relationship only allows one record to be connected to one other record.
    <br>
    <br>
    <strong>Which other table in your database will likely have a one-to-one relationship with the employees table?</strong>
    <br>
    the badges table
    <br>
    Every single badge should be associated with a single employee.
</details>

<details>
    <summary><strong>Database Optimization Quiz</strong></summary>
    <strong>Second Normal Form tells you to _____ in addition to being compliant with First Normal Form.</strong>
    <br>
    ensure that no non-key field is dependent on only part of a composite key
    <br>
    Before you get to 2NF, you need to make sure your tables have no repeating groups.
    <br>
    <br>
    <strong>If you can figure out the value of one non-key field in a row by looking at another non-key field in that same row, what do you violate?</strong>
    <br>
    Third Normal Form
    <br>
    3NF tells you that each field in a row should represent something unique about a record.
    <br>
    <br>
    <strong>In order to put a database into Third Normal Form, _____.</strong>
    <br>
    it must also be in First and Second Normal Form
    <br>
    Normalization is a progressive process, and higher forms depend on the database being compliant with lower forms as well.
    <br>
    <br>
    <strong>What does denormalization refer to?</strong>
    <br>
    consciously choosing to violate the rules of normality in order to improve speed or for some other business reason
    <br>
    Denormalization is usually a trade-off between speed and integrity.
    <br>
    <br>
    <strong>First Normal Form tells you to do what?</strong>
    <br>
    remove repeating groups
    <br>
    If you find yourself adding lists of things in individual fields or adding columns to represent additional fields of the same type, you're probably creating repeating groups. And 1NF tells you that you need to refactor your tables if that happens.
    <br>
    <br>
    <strong>When might you choose to denormalize a table?</strong>
    <br>
    Retrieving the data upon request would be slow or burdensome, and you are able to pre-calculate or store a copy of the data somewhere it can be retrieved faster.
    <br>
    If you need to prioritize the speed of a particular operation, you might choose to denormalize, as long as you remain aware of the threat to database integrity.
    <br>
    <br>
    <strong>What does normalization help you do?</strong>
    <br>
    accomplish all of these goals
    <br>
    The normalization process provides a framework to think about how data is organized.
    <br>
    <br>
    <strong>A table has two rows with the same values in all columns. Which step can you take to have this table meet the first normal form (1NF) requirements?</strong>
    <br>
    Add a primary key to the table.
    <br>
    The primary key will add a unique value for each row, and thus eliminate the repeating duplicate rows issue.
</details>

<details>
    <summary><strong>Querying a Database Quiz1</strong></summary>
    <strong>What is the foreign key in the table created after this command?</strong>

```
CREATE TABLE Models (
ModelID INT(6) NOT NULL AUTO_INCREMENT,
Color INT(6) REFERENCES Colors(ColorID),
PRIMARY KEY(ModelID)
);
```
Color
    <br>
    <br>
    <strong>Which SQL command will you use to create a new database called "mydb"?</strong>

``CREATE DATABASE mydb;``
The "CREATE DATABASE" command is used to create a new database.
    <br>
    <br>
    <strong>Which of these is not an example of a time when you would use an aggregate function?</strong>
    <br>
    looking up customers with the name Rafael Montresso
    <br>
    Aggregate functions are used to tell you about certain characteristics of multiple records. Requesting a record by specific field values is not an aggregate operation.
    <br>
    <br>
    <strong>Which WHERE condition can you use to find all records containing a first name starting with the letter "A"?</strong>

``WHERE FirstName LIKE "A%";``
The percent symbol is used as a wildcard for anything coming after the letter "A."
    <br>
    <br>
    <strong>When using an aggregate function, how many results do you expect?</strong>
    <br>
    one
    <br>
    Aggregate functions return one value that describes a set of data.
    <br>
    <br>
    <strong>What should come instead of the ??? placeholder for this query to return all fields and records in the table?</strong>

``*``
The asterisk is used as a wildcard to retrieve everything from the given table.
    <br>
    <br>
    <strong>In any given query, you can only join together a maximum of two tables.</strong>
    <br>
    FALSE
    <br>
    You can join together many tables as long as you tell the database which pairs of values on the tables are intended to match.
    <br>
    <br>
    <strong>In order to use records from more than one table in a query, you need to _____ the tables based on some matching criteria.</strong>
    <br>
    join
    <br>
    Joining tables allows you to match rows from one table with rows on another table.
    <br>
    <br>
    <strong>If a table is set to auto-increment the primary key, you'll need to know the next value and set it manually when you enter a record.</strong>
    <br>
    FALSE
    <br>
    When the database automatically increments a key field, you don't need to worry about setting the value. The database will provide the next value in the sequence automatically.
    <br>
    <br>
    <strong>When modifying a record, it's a good idea to specify the record _____.</strong>
    <br>
    as precisely as possible, ideally using the primary key
    <br>
    If you've designed your database correctly, each record should have a key that uniquely identifies it, making it safe to use that key to modify a record.
    <br>
    <br>
    <strong>In order to sort results based on a field, that field needs to appear in the final output.</strong>
    <br>
    FALSE
    <br>
    <br>
    <strong>A SQL statement that returns requested records from the database is called:</strong>
    <br>
    a SQL query
    <br>
    All statements return a status when executed, but a query is a special case of statement that returns information you asked for.
    <br>
    <br>
    <strong>You can write SQL:</strong>
    <br>
    all of these answers
    <br>
    You can write SQL statements in any of these places.
    <br>
    <br>
    <strong>You can narrow down the results that a query returns by only asking for results where a _____ matches a given value.</strong>
    database
    <br>
    <br>
    <strong>Which of these tasks can you accomplish using SQL as a DML?</strong>
    inserting a record into a table
    <br>
    Inserting a record is a data manipulation task.
    <br>
    <br>
    <strong>When first defining a table, what should you specify? (find 3 correct items)</strong>
<br>
A.   the table's name
<br>
B.   the table padding
<br>
C.   the fields and type of data they contain
<br>
D.   the data per cell
<br>
E.   the primary key and any referential constraints
<br>
<br>
A, C, E
<br>
Without this information, you can't fully define a table.
    <br>
    <br>
    <strong>Which sorting option shows dates from latest to earliest?</strong>

``ORDER BY `Date` DESC``
The DESC option will sort in descending order and show the latest dates first.
    <br>
    <br>
    <strong>When you use SQL statements to create or modify the structure of a database, what is SQL being used as?</strong>
    <br>
    a Data Definition Language (DDL)
    <br>
    As a Data Definition Language, SQL can be used to create and modify the structure of database tables.
    <br>
    <br>
    <strong>What is the correct SQL syntax to use when joining tables A and B on their "ID" field?</strong>
    <br>

```
SELECT * FROM A
JOIN B ON A.ID=B.ID
```
The join statement specifies the field on which the two tables will be joined.
    <br>
    <br>
    <strong>When telling the database that a certain field must not contain an empty value, you say that it is:</strong>
    <br>
    not null
    <br>
    For some fields, you might want to prohibit entering records with empty values. By telling the database that the field can't be null, the database will handle this restriction for you.
    <br>
    <br>
    <strong>For a table that holds the purchase amounts in a grocery store over time, which query will likely return the highest value?</strong>
    <br>

``SELECT SUM(amount) FROM purchases;``
The purchase amounts will grow over time and add up to a very large sum.
    <br>
    <br>
    <strong>What is the possible issue with this query?</strong>

``UPDATE mytable SET price=5;``
It may update undesired records.
<br>
Without a WHERE condition, this query will update all records including possibly undesired ones.
</details>

<details>
    <summary><strong>Querying a Database Quiz2</strong></summary>
    <strong>Which database is often used in a big data context?</strong>
    <br>
    Hadoop
    <br>
    Hadoop and Spark are often used for big data applications.
    <br>
    <br>
    <strong>Microsoft Access is generally considered a(n) _____ database platform.</strong>
    <br>
    desktop
    <br>
    Desktop databases are typically hosted on a workstation rather than a dedicated server, and they're designed to support a few to a few hundred users.
    <br>
    <br>
    <strong>Relational databases can store all of these except what?</strong>
    <br>
    graph data
    <br>
    <br>
    <strong>A stored procedure is _____.</strong>
    <br>
    a predefined query or statement
    <br>
    Stored procedures are queries that are stored on the server, and they can be called by developers or users in their queries.
    <br>
    <br>
    <strong>An index _____.</strong>
    <br>
    helps to increase the speed of lookups using a particular column at the cost of speed while modifying records
    <br>
    As with denormalization, indexes offer a trade off.
    <br>
    <br>
    <strong>What is it called when a malicious user tries to change the way a SQL statement works by entering their own SQL?</strong>
    <br>
    injection
    <br>
    This kind of attack involves someone injecting their own code into an application.
    <br>
    <br>
    <strong>If you store certain kinds of information, your database may be subject to certain compliance regulations.</strong>
    <br>
    TRUE
    <br>
    If you store personally identifiable information (PII), health information, or some other kinds of information, your database may be subject to various regulations. Be sure to do your research and stay in compliance!
    <br>
    <br>
    <strong>What is a database transaction?</strong>
    <br>
    a group of statements that runs or fails as a whole
    <br>
    Transactions combine multiple statements into a single logical block, where one failing statement rolls back the entire action.
</details>