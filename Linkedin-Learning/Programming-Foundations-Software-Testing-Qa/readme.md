## Programming Foundations Software Testing QA


### Introduction
#### Specialists in software Testing
* QA
* QA enginner
* QA analyst
* software enginner in test
* Tester

Ensure the team is building the right product
Help their team move quickly with confidence
They establish and maintain standards

#### How to ensure quality
* Clear specifications
* Code implemented
* Code Tested
* Code released


### The Role of QA
#### Roles and responsibilities
* Teachincal aptitude
* Business knowledge
* DevOps principles
* Process and release expertise

__Teachincal aptitude__
* Manual testing
* Automated testing
* Programming
* Scripting
__Business knowledge__
* Feature scoping
* Test planning
* Test case management
* Bug management
__DevOps Principles__
* Configure tools
* Set up CI
* Set up test environments
* Automate processes
__Process and release expertise__
* Define and improve testing practices
* Optimize release process

#### Get involved throughout the SDLC
__SDLC__
* Plan
* Define
* Design
* Build
* Test
* Deploy

__plan__
* Identify risks
* Identify use cases
__Define__
* Write specs and acceptance criteria
* Decide what's in scope
* Write test strategy
__Design and Build__
* Soldify test scenarios
* Get feedback on scenarios from team
* Manual and automation tests
__Test__
* Manual and automation tests
* Acceptance testing
__Deploy__
* Validate functionality
* Release
* Test in production


#### Collaborate with the team
__SDLC__
* Plan   (QA, biz, dev, design)
* Define (QA, biz, dev, design)
* Design (QA, biz, dev, design)
* Build  (dev, QA, design)
* Test   (dev, QA, design)
* Deploy (dev, QA, biz)

* Build a relationship with your teammates
* Know the responsibilities of each role
* Collaborate
Share what it means to be a software tester

#### Set expectations and goals
__Sharing Goals__
* Accountability
* Awareness
* Support

Communicate what you are working on
ASk for help
Give and receive feedback

#### Write acceptance criteria
__acceptance criteria__
Conditions that a software product must satisfy to be accepted by a stackholder

Example
__User story: add a sold out item to a cart__
* Given I am viewing an item
* When I press the ADD TO CART button
* Then the item is added to the cart

__User story: add a item to a cart__
* Given I am viewing an item that is sold out
* When I press the ADD TO CART button
* Then the item is not added to the cart
* And I see a message that the item is out of stock


### Types of testing QA Focuses on
#### Box testing
* Black box testing
* Gray box testing
* White box testing

__Types of Black box tests__
* Manual
* UI automation

when the box is completely concealed and it is not possible to see inside of it.

It allows input to the box and gets output from the box.

we don't need knowledge about the internals of the application,
such as what the source code is doing or how the system is working.

focus with black box testing is to perform an action in the user interface
and expect a certain result from that action.

QA engineers are responsible for this level of testing.

__Types of Gray box tests__
* Integration testing
* Tigger some action in the UI

Here the box is semi-transparent.

Test scenarios here examine the interaction between the outside and inside of the box.

It requires QA engineers to have a deeper understanding of the application.

QA engineers and developers are responsible for these level of test.

__Types of White box tests__
* Unit
* Sysytem

 Here the box is completely transparent
the focuses on the internals of the application
and what is happening at the code or system level.

__Tset Scenario__
* The quantity can be increased
* The quantity can be decreased
* The quantity can be items is correct

#### Manual testing
Manual testing follows the steps as a user performing workflows in the application

The goal is to uncover any issues in the functionality and usability.
Before performing manual testing know what scenarios you want to cover.

Identify __test scenarios__ before testing.
Identify both typical and nontypical use cases

__Happy Path Scenarios__
* Search for one-way flight
* Search for round-trip flight

__Sad Path Scenarios__
* Search for same origin and destination
* Search for invalid route
* Search for route not in operation

#### UI automation testing
is like manual testing but uses a script to automate test scenarios.
The benefit of UI automation is that scenarios can be executed repeatedly by running a test script.
This will help catch regressions and other oddities much quicker than when done manually
Another benefit is that the scripts can be run on any platform or browser

__Benefit of UI Automation__
Scenarios can be executed repeatedly and catch regressions introduced in the application

__Intergration testing__ focuses on the interaction between application components

__Presentation layer__
HTML, CSS, JS
__Applcation layer__
Code
__Data layer__
Server, database

#### Performance testing
Performance testing is done to benchmark how a system performs under load.
  It will help ensure that an application can scale over time and use.
  Is a type of black box testing

__Performance testing__ benchmarks how a system performs under load
__Performance testing__ is done to make sure an application runs fast and well

* Load testing
* Stress testing
* Securtiy testing

__Load testing__ checks the application's ability to perform under user loads
Endurance testing checks how an application handles load over time
Goal of endurance testing is to check for system problems

__Endurance testing__ checks how an application handles load over time the goal of it is to check for system problems

__Stress testing__ involves testing an application under extreme workloads. it is used for testing scalability

Goal of stress testing is to measure software stability
when does it fail?
How does it recover?

__Common Performance Problems__
* Long load time
* Poor scalability
* Bottlenecking

#### Security Testing
__Securtiy testing__   is performed to reveal flaws or vulnerabilities that can be exposed by users.
Exposes problems in the application that can cause unexpected behavior or crashes.

__SQL Injection__
SQL injection is used to insert database statements into text fields and expose application information

__Denial of Service (DoS)__
Denial of service is an attack where hackers try to take down an application's servers or netwrok

__Vulnerabilities__ in dependencies can cause massive securtiy problems


### Bug reporting
__Bugs__
  are inevitable. They occur when the system does not work as designed or specified,
  and result in incorrect or unexpected behavior in an application.

__Bugs are versatile.__
* They can be low impact or high impact,
* they can affect many users or just a handful of users,
* they can be constantly reproducible or not,
* and some bugs even go away and come back later.
