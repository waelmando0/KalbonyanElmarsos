## Programming Foundations: object oriented Fundamentals

### Object-Oriented Fundamentals
<details>
		<summary><strong>Object oriented thinking</strong></summary>
		relaize that object oriented programming is not itself a language Object orientation
		is referred to as a programming paradigm A set of ideas that's supported by many
		languages
		<br>
		<br>
        <strong>Object-Oriented Programming (OOP): </strong>
		<br>
		is a programming paradigm that relies on the concept of <strong>classes and objects.</strong> It is used to structure a software program into simple, reusable pieces of code blueprints <strong>(usually called classes)</strong>, which are used to create <strong>individual instances of objects.</strong>
        <br>
		<ul>
			<li>Objects contain both functions (or methods) and data.</li>
			<li> An object provides a public interface to other code that wants to use it, but it maintains its own private internal state: this means that other parts of the system don't have to care about what is going on inside the object.</li>
		</ul>
        <br>
		<strong>Object oriented Programming Language</strong>
		<ul>
			<li>C#</li>
			<li>C++</li>
			<li>Go</li>
			<li>Java</li>
			<li>Javascript</li>
			<li>perl</li>
			<li>PHP</li>
			<li>python</li>
			<li>R</li>
			<li>Ruby</li>
			<li>Swift</li>
			<li>VB.NET</li>
			<li>and many others</li>
		</ul>
		<br>
		And there are other programming paradigms beyon just procedural and object
		orientation
		<ul>
			<li><strong>Logic Programming Language:</strong> Like Prplog</li>
			<li><strong>Functional Programming Language:</strong> Like Haskell</li>
		</ul>
</details>
<details>
		<summary><strong>Classes</strong></summary>
		<strong>Class: </strong>code-template for creating program objects
		<br>
		<br>
		<strong>Class Components</strong>
		<ul>
			<li><strong>Type ➡️ Name:</strong> What is it?
			<br>
			"RoundCookie"
			</li>
			<li><strong>Properties, data ➡️ Attributes:</strong> What describes it?
			<br>
			"Weight, Color"
			</li>
			<li><strong>Operations ➡️ Behavior:</strong> What can it do?
			<br>
			"decorate() - consume()"
			</li>
		</ul>
		<br>
		<strong>Method:</strong> are basically functions with key difference that methods
						are defined as part of a class
		<ul>
			<li>A program procedure that can return a value </li>
			<li>Defined as part of a class</li>
			<li>can only access data known to its object</li>
		</ul>
		<br>
		<strong>Example</strong>

```
Class Feel:
	position
	color
	boolean
	move()
```
<br>
		<strong>Existing Classes in OO Languages</strong>
		At a minimum:
		<br>
		<ul>
			<li>strings</li>
			<li>Dates</li>
			<li>Collections</li>
			<li>File I/O</li>
			<li>Networking</li>
			<li>And often many more...</li>
		</ul>
		<br>
		<strong>Frameworks and libraries</strong>
		<ul>
			<li>Java Class Library</li>
			<li>.NET Framework BCL</li>
			<li>C++ Standard Library</li>
			<li>Ruby Standard Library</li>
			<li>Python Standard Library</li>
		</ul>
</details>
<details>
		<summary><strong>Object</strong></summary>
		<strong>Object</strong> is an instance of a class
		<br>
		<br>
        Objects are class instances that inherit all the variables and methods from a class.
        <br>
		All objects have
		<ul>
			<li><strong>Identity:</strong>  Coffee mug</li>
			<li><strong>Attribute:</strong> Color, size, fullness</li>
			<li><strong>Behviors:</strong>  fill(), empty(), clean()</li>
		</ul>
		<br>
		<storng>Example</storng>

```
Feel = new Feel(3, "white", false)
```
<br>
		<strong>Objects = Nouns</strong>
		<ul>
			<li>Things</li>
			<li>People</li>
			<li>Places</li>
			<li>Ideas</li>
			<li>Concepts</li>
		</ul>
</details>
<details>
		<summary><strong>Four Principles of OOP</strong></summary>
		there are four fundamentals ideas in object oriented programming to keep in your
		mind when creating classes
		<ul>
			<li><strong>Encapsulation: </strong>containing information in an object, exposing only selected information</li>
			<li><strong>Abstraction: </strong>only exposing high level public methods for accessing an object</li>
			<li><strong>Inheritance: </strong>child classes inherit data and behaviors from parent class</li>
			<li><strong>Polymorphism: </strong>many methods can do the same task</li>
		</ul>
</details>
<details>
		<summary><strong>Encapsulation</strong></summary>
		<strong>Encapsulation:</strong> is the packing of data and functions into one component (for example, a class) and then <strong>controlling access to that component to make a "blackbox" out of the object.</strong>
		<br>
		<br>
		<ul>
			<li>Wrapping up a data and method together into a single unit (in other words class) is called Encapsulation</li>
			<li>Encapsulation is like enclosing in a capsule. That is enclosing the related operations and data related to an object into that object</li>
		</ul>
		<br>
		the purpose of encapsulation is to protect an object from unwanted changes
		<br>
		<strong>to protect an object from unwanted changes to have access to the that data you should use methods that object have setter method or getter method that you define</strong>
		<br>
		<br>
        to make sure that "sensitive" data is hidden from users. To achieve this, you must declare class variables/attributes as private (cannot be accessed from outside the class). If you want others to read or modify the value of a private member, you can provide public get and set methods.
		<br>
		<br>
        <strong>Why Encapsulation?</strong>
        <ul>
            <li>Encapsulation ensures better control of your data, because you (or others) can change one part of the code without affecting other parts</li>
            <li>Increased security of data</li>
        </ul>
		<br>
		<strong>Example</strong>

```
class Player:
 currentHealth
 maxHealth
 setHealthOnLevelUp():
  maxHealth += 500
  currentHealth = maxHealth
```
<br>
		<strong>Another Example</strong>

```
class Car:
 gastype = diesel
 getFuelPercentage():
  return Fuel%
```
<br>

```
bmw = new Car()
bmw.getFuelPercentage()
```
</details>
<details>
		<summary><strong>Abstraction</strong></summary>
		<strong>Abstraction: </strong>main goal is to handle complexity by hiding unnecessary details from the user.
        <br>
		Abstraction means we focus on the essential qualities of something rather than one specific example. By using abstraction, we automatically discard what's unimportant or irrelevant.
		<br>
        Hiding unnecessary details and functionalities and only showing what is important to work is an abstraction.
        <br>
        <br>
		<ul>
			<li>Abstruction is "To represent the essentail feature without representing the background details" </li>
			<li>Abstruction lets you focus on what the object does instead of how it does it</li>
		</ul>
        <br>
        refers to “showing” only the essential attributes of something and “hiding” any implementation information that is unnecessary to the user.
        <br>
        <br>
        It allows users not to get overwhelmed by the hidden logic that makes the users complex logic.
        <br>
        the user is not required to understand or even think about it.
        <br>
        <br>
        <strong>Advantages of Data Abstraction</strong>
        <ul>
            <li>Helps the user to avoid writing low level code.</li>
            <li>Avoids code duplication and increases reusability.</li>
            <li>Can change internal implementation of class independently without affecting the user.</li>
            <li>Helps to increase security of an application or program as only important details are provided to the user.</li>
        </ul>
</details>
<details>
		<summary><strong>Inheritance</strong></summary>
		<strong>Inheritance: </strong>it is possible to inherit attributes and methods from one class to another.
		<br>
        <strong>parent classes extend attributes and behaviors to child classes.</strong>
		<br>
		<br>
        <strong>inheritance concept</strong> into two categories:
        <ul>
            <li><strong>derived class (child)</strong> - the class that inherits from another class</li>
            <li><strong>base class (parent)</strong> - the class being inherited from</li>
        </ul>
		<br>
		<ul>
			<li>Base a new object or class on an existing one</li>
			<li>Inherit the existing attributes and methods</li>
			<li>Great form of code reuse</li>
		</ul>
		<br>
		<strong>Why And When To Use "Inheritance"?</strong>
		<br>
        <strong>It is useful for code reusability:</strong> reuse attributes and methods of an existing class when you create a new class.
		<br>
		<br>
		Multiple Inheritance: mean one child has more than father it's not good and not supported in all the language
</details>
<details>
		<summary><strong>Polymorphism</strong></summary>
		<strong>Dynamic Polymorphism: </strong>Uses the same interface for methods on different types of objects that may implement those method in different ways
		<br>
		<br>
		<strong>Method Overriding:</strong> is change one or more methods from the superClass with the same name to take the same input but change the function itself.
		<br>
		<strong>Creating a unique version of an inherited method.</strong>
		<br>


```
Animal:
 makeSound()

cat:
 makeSound() → "Meow"

dog:
 makeSound() → "Haw haw"
```
<br>
		<strong>Method Overloading: </strong>Implements multiple methods with the same name, but different parameters
		<br>
		Example:

```
brew(coffee, water) → cupOfCoffee
brew(tea, water) → cupOfTea
brew(coffee, tea, water) → cupOfSomething
```
</details>

<details>
		<summary><strong>Analysis, design, and programming</strong></summary>
		<strong>Object-Oriented:</strong> there are usually another word right beside it
		<ul>
			<li><strong>Object Oriented Programming:</strong> Built it, The way to built your design</li>
			<li><strong>Object Oriented Design:</strong> Plan your solution, How are you going to do it?</li>
			<li><strong>Object Oriented Analysis:</strong> Understand your problem, What you need to do?</li>
		</ul>
		<br>
		<strong>The five steps approach:</strong>
		<ul>
			<li>1. Gather requirements ( Fetching for a problem to solve)</li>
			<li>2. Describe the application ( Plain text of how the people will use it)</li>
			<li>3. Identify the main object (The start point of making the classes)</li>
			<li>
				1. Describe the interactions between them
				<ul>
					<li>1. Understanding each object responsibilities.</li>
					<li>2. The behaviors they need to have.</li>
					<li>3. When they interact with other objects</li>
				</ul>
			</li>
			<li>5. Create a class diagram</li>
		</ul>
</details>
<details>
		<summary><strong>Unified modeling language (UML)</strong></summary>
		<strong>Unified Modeling Language (UML):</strong> Standardized notation for diagrams to visualize object-oriented systems.
		<br>
		<h4>Types of UML Diagrams</h4>
		<strong>Structural Diagrams</strong>
		<ul>
			<li>Class diagram</li>
			<li>Component diagram</li>
			<li>Depolyment diagram</li>
			<li>Object diagram</li>
			<li>Package diagram </li>
			<li>Profile diagram </li>
		</ul>
		<br>
		<strong>Behavioral Diagrams</strong>
		<ul>
			<li>Use case diagram</li>
			<li>Activity diagram</li>
			<li>State machine diagram</li>
			<li>sequence diagram</li>
			<li>Communication diagram </li>
			<li>Interaction overview diagram </li>
			<li>Timing diagram </li>
		</ul>
		<br>
		<h4>UML Tools</h4>
		<strong>Things to consider</strong>
		<ul>
			<li>Commercial or open source</li>
			<li>Support platforms</li>
			<li>Diagram drwaing capabilites</li>
			<li>Code generation capabilites</li>
		</ul>
</details>

### Requirements
<details>
		<summary><strong>Defining Requirements</strong></summary>
		The first step to any design process is to gather your requirements.
		<br>
		Figure out what your application or product needs to do.
		<br>
		<br>
		<strong>Requirements</strong> = what does the program need to do ?
		<br>
		what is the problem you are trying to solve ?
		<br>
		why are you building the program in the first place?
		<br>
		<br>
		<strong>Funcational Requirements:</strong> = What must it do?
		<br>
		the application must do ......
		<br>
		<br>
		Example: The system must:
		<ul>
			<li>Heat meals in space-packaging</li>
			<li>Allow users to set a timer for the meal</li>
			<li>Notify the user when the meal is ready.</li>
			<li>Change cooking time based on the type of meal</li>
			<li>Continue to function without a network connection</li>
		</ul>
		<br>
		<strong>Non-functional</strong> requirements = How should it do it?
		<ul>
			<li>Is it <strong>legal?</strong></li>
			<li><strong>Performance:</strong> Response time, Users Number simultaneously.</li>
			<li><strong>Support:</strong> if some problems happen any time what will you do?</li>
			<li><strong>Security</strong></li>
		</ul>
		<strong>How should be:</strong>
		<ul>
			<li>Available 24/7</li>
			<li>Usable while wearing work gloves.</li>
		</ul>
</details>

<details>
		<summary><strong>FURPS+ requirements</strong></summary>
		<strong>FURPS</strong> One commonly used model for classifying software quality attributes
		<br>
		FURPS serves as a checklist of several key qualities to consider when determining requirements.
		<br>
		<br>
		<strong>FURPS refer to </strong>
		<ul>
			<li>
				<strong>Functionality: </strong>the Features of the app
				<br>
				Capability, Reusability, Security
			</li>
			<br>
			<li>
				<strong>Usability: </strong>what affect the person who will use the app?
				<br>
				Is it easy on the eyes?
				<br>
				 Is it intuitive to use?
				<br>
 				Is the documentation accurate and complete?
				<br>
				Human Factors, Aesthetics, Consistency, Documentation
			</li>
			<br>
			<li>
				<strong>Reliability: </strong>How Much system downtime is acceptable? Is system can be recovered?
				<br>
				Availability, Failure Rate & Duration, Predictability
			</li>
			<br>
			<li>
				<strong>Performance: </strong> dictate the application's response time through put.
				<br>
  				And they put limits on the system resources it can use. In supportability.
  				<br>
				Speed, Efficiency, Resource, Consumption, Scalability
			</li>
			<br>
			<li>
				<strong>Supportability: </strong>  Make sure the application can be tested, extended, serviced and installed and configured.
				<br>
				Testability, Extensibility, Serviceability, Configurability
			</li>
		</ul>
		<br>
		<strong>FURPS+</strong>
		<ul>
			<li><strong>Design: </strong>constraints on how the software must be built because the app requires certain things such as a relational database.</li>
			<li>
				<strong>Implementation: </strong> Does it have to be written in a certain language?<br>
				Are there standards or methodologies that need to be followed?</li>
			<li>
				<strong>Interface: </strong>Communication with other devices is a common need.
				<br>
				refer to an external system that needs to be interfaced with.
			</li>
			<li><strong>Physical: </strong> related to the hardware on which the application must run or deplyed on.</li>
		</ul>
</details>
<details>
	<summary><strong>Solution: Jukebox requirements</strong></summary>
	<strong>Functional - the system must do:</strong>
	<ul>
		<li>Have music libraries</li>
		<li>Allow user to choose any album and select single song</li>
		<li>After putting any song to play check the queue</li>
		<li>if the last 3 songs from same user jump it to the next play</li>
		<li>if not put it in the queue</li>
	</ul>
	<br>
	<strong>Non-Functional - the system should be:</strong>
	<ul>
		<li>Intuitive to use while floating in space</li>
		<li>Available 24/7</li>
		<li>Low power</li>
	</ul>
</details>

### Use Cases and User Stories
<details>
	<summary><strong>Use cases</strong></summary>
	<strong>Use Cases: </strong>shifting focus towards the user and how they accomplish a particular goal a use case needs three essential things
	<br>
	<ul>
		<li><strong>Title: </strong>What is the goal?</li>
		<li><strong>Primary Actor: </strong>Who desires it? (the person or system that will use the program)</li>
		<li><strong>Success Scenario: </strong>How is it accomplished? (the steps)</li>
	</ul>
	<strong>Additional Details</strong>
	<ul>
		<li><strong>Preconditions:</strong> When this use case is started?</li>
		<li><strong>Postconditions</strong></li>
		<li><strong>Secondary Actors</strong></li>
		<li><strong>Stakeholders</strong></li>
		<li><strong>Scope</strong></li>
		<li><strong>Priority</strong></li>
		<li><strong>Owner</strong></li>
	</ul>
	<br>
	<h4>Use Case: Scenario as Steps</h4>
	<ul>
		<li><strong>Title: </strong>Heat Meal</li>
		<li><strong>Primary Actor: </strong>Astronaut</li>
		<li>
			<strong>Success Scenario: </strong>
			<ul>
				<li>Astronaut inserts meal package.</li>
				<li>The system identifies the type of meal.</li>
				<li>The system heats the package for the length of time required for meal type.</li>
				<li>The system notifies the astronaut that the meal is ready to vie space pager.</li>
				<li>Astronaut removes the package from the system.</li>
			</ul>
		</li>
		<li>
			<strong>Extensions</strong>
			<ol>
				<li>Describe steps for unidentifiable package</li>
				<li>Describe steps for space-pager system error</li>
			</ol>
		</li>
	</ul>
</details>
<details>
	<summary><strong>Identifying the actors</strong></summary>
	Start thinking about the peoples who maybe use your system "If it multiple users system". (User Icon)
	<br>
	who will interact with the program
	<br>
	Thinking about another systems or organizations which need to connect with your system. (Systems = Box)
	<br>
	Notice that  the program could have multiple people interacting with it to accomplish different goals.
	<br>
    Thinking about their different job titles or departments can also prompt ideas for use case scenarios.
	<br>
	yoou should also ask does the application need to interact with other computer systems or other organizations?
	<br>
    Those external systems are considered actors too.
	<br>
	But keep in mind that the same person with the same role and job title could actually be different actors at different times.
	<br>
    The focus should really be on the goal that the actor wants to accomplish, and how we define those actors can vary depending on the use case.
	<br>
    the primary actors in scenario aren't necessarily the most important actor in the scenario They're just the one who initiated it
</details>
<details>
	<summary><strong>Identifying the scenarios</strong></summary>
	describe a goal that an actor can accomplish in a single encounter and stay focused on the user's intention what they really want to accomplish.
	<br>
	<br>
	write your scenario either as a paragraph or a list of steps The goal is readability and ease of creation over formality.
	<br>
    don't put the verbs that will accomplish the goal put the goal it self omit needless words
    don't use words like screen, click, button , select
	<strong>User-Focused Goals</strong>
	<ul>
		<li>Cook meal</li>
		<li>Generate reports</li>
		<li>Change settings</li>
		<li>Order supplies</li>
	</ul>
	<br>
	<strong>Focus</strong> only on the best scenario ever then all others can be alternative paths
	<br>
	<strong>Focus</strong> on the main actions with out any details
	<br>
	<strong>Focus</strong> on the function without the interface, Don't use words bottom, screen, click .. etc.
	<br>
	<br>
	<strong>Question to help you thinking:</strong>
	<ul>
		<li>Who performs system adminstration tasks?</li>
		<li>Who manages users and security?</li>
		<li>What happens of the system fails?</li>
		<li>Is anyone looking at performance metrics or logs?</li>
	</ul>
</details>
<details>
	<summary><strong>Diagramming use cases</strong></summary>
	<ol>
		<li>Start with listing your use cases</li>
		<li>Then draw the actors with there names, and make circle on each use case, after than draw a big box around use cases as a refer to the system internal</li>
		<li>Draw lines from the actor to each user case he will work with</li>
		<li>If there are another system or second role actor, draw it at the other side with square around and <<actor>> to define it</li>
	</ol>
</details>
<details>
	<summary><strong>User stories</strong></summary>
	User story is simpler than use case, it's focus only on small scenario from the user perspective and focusing only on his goal. As a (type of user) I want (goal) so that (reason)
	<br>
	still describes a single small scenario from a user's perspective, focusing on their goal. what they want to do and why rather than focusing on the system.
	<br>
	But unlike a use case, which can be several pages,
	<br>
	a user story is typically written as just one, perhaps two, sentences and they're very commonly written on index cards because that forces us to keep them short and sweet.
	<br>
	the focus is on intent and should not include descriptions of the user interface. these are intended to be quick, readable summaries of a specific goal and why the user wants it.
	<ul>
		<li>
			As an astronaut - I want to heat up my food - So that I can get eat a warm meals
		</li>
		<li>
			As a nutritianist - I want to see what astronauts eat - So that i can monitor their diet
		</li>
		<li>
			As an astronaut - I want to press a button to delay when my food gets cooked - So that it will be ready later
		</li>
		<li>
			As an astronaut - I want to schedule when i heat my food- So it will be ready later
		</li>
		<li>
			As a student - I want to see my courses - so I can focus on studying.
		</li>
	</ul>
	<br>
	<br>
	<table>
		<tr>
			<th>User Stories</th>
			<th>Use Cases</th>
		</tr>
		<tr>
			<td>short (one index card)</td>
			<td>Long (a document)</td>
		</tr>
		<tr>
			<td>One goal, no details</td>
			<td>Multiple goals and details</td>
		</tr>
		<tr>
			<td>Informal</td>
			<td>Casual to (very) formal</td>
		</tr>
		<tr>
			<td>"Placeholder for conversation"</td>
			<td>"Record of converstion"</td>
		</tr>
	</table>
	<br>
	We start making User Stories to hold the topics then make Use case to Each one or collect smaller together.
</details>
<details>
	<summary><strong>Challenge: Jukebox use cases</strong></summary>
	<strong>Functional Requirements</strong>
	<ul>
		<li>Maintain a library of albums/songs</li>
		<li>Allow users to brows albums/songs</li>
		<li>Allow users to select individual songs</li>
		<li>Prevent users from selecting entire albums</li>
		<li>Maintain a queue of songs to play</li>
		<li>Play music</li>
		<li>Allow users to sort by artist</li>
		<li>Identify individual users</li>
		<li>Track number of plays per user</li>
	</ul>
	<br>
	<strong>Non-Functional Requirements</strong>
	<ul>
		<li>Intuitive to use in spacec</li>
		<li>Available 24/7</li>
		<li>Low Power</li>
		<li>Updatable</li>
	</ul>
	<br>
	<strong>Use Case 01</strong>
	<ul>
		<li><strong>Title: </strong>Play song</li>
		<li><strong>Primary Actor: </strong>User</li>
		<li>
			<strong>Success Scenario: </strong>
			<ol>
				<li>The system identifies user</li>
				<li>The user browses library of available albums</li>
				<li>The user selects an album and browses list of songs on the selected album</li>
				<li>The user selects a song</li>
				<li>The system plays the selectd a song</li>
				<li>play like setting</li>
			</ol>
		</li>
	</ul>
	<br>
	<strong>Use Case 02</strong>
	<ul>
		<li><strong>Title: </strong>Select Multiple Songs</li>
		<li><strong>Primary Actor: </strong>User</li>
		<li>
			<strong>Success Scenario: </strong>
			<ol>
				<li>The system identifies user</li>
				<li>The user browses available albums and songs</li>
				<li>The user selects a song</li>
				<li>The system begins playing selectd song</li>
				<li>The user continues browsing and selects a second song</li>
				<li>The system adds second song to play queue</li>
				<li>The system plays second song after first song is over</li>
			</ol>
		</li>
	</ul>
	<br>
	<strong>Use Case 03</strong>
	<ul>
		<li><strong>Title: </strong>Play song</li>
		<li><strong>Primary Actor: </strong>Astronaut</li>
		<li>
			<strong>Success Scenario: </strong>
			<ol>
				<li>Astronaut open lib</li>
				<li>Then pick an album</li>
				<li>
					choose 3 songs or less to play
					<ol>
						<li>if choose more tell him max number</li>
						<li>if there are 3 same user jump next play</li>
					</ol>
				</li>
				<li>
					choose play setting (loop, shuffle)
					<ol>
						<li>if not selected ask after queue, time 10sec then shuffle.</li>
					</ol>
				</li>
				<li>play like setting</li>
			</ol>
		</li>
	</ul>
	<br>
	<br>
	<strong>Use Case 04</strong>
	<ul>
		<li><strong>Title: </strong>Update Lib</li>
		<li><strong>Primary Actor: </strong>Admin</li>
		<li>
			<strong>Success Scenario: </strong>
			<ol>
				<li>Astronaut open sittings</li>
				<li>plugin storage</li>
				<li>move new data, done editing</li>
				<li>remove storage</li>
				<li>close setting</li>
			</ol>
		</li>
	</ul>
	<br>
	<strong>User Stories</strong>
	<br>
	As a user, i want my song to be added to the front of a long play queue, so that i don't have to wait hours to hear it
	<br>
	As a user, i want to be identified without touching anything, so that my hands are free to do other things
</details>

### Domain Modeling

<details>
	<summary><strong>Identifying the objects</strong></summary>
	- After defining requirements and writing some use cases or user stories we start to transition from analysis, understanding the problem we're trying to solve, to design, how we're going to organize our solution.
  	<br>
	- with the analysis done, our next step is to create a conceptual model.
	<br>
	<br>
	<strong>Conseptual Model: </strong> Represents important objects and the relationships between them
	<br>
	This model is done after analysis phase (Use cases & user stories)
	<br>
	at this point we pick all our system objects and every thing we should be aware of
	<br>
	To get the objects we go back to the use cases and the user stories then pick all of the nouns
	<br>
	To identify objects we'll go through all of our use cases and user stories and any other written requirements to pick out all of the nouns.
	<br>
  	after defining the objects we simply drawing a box around each of those objects we have the beginning of a conceptual model.
	<br>
	<img src="https://manssorr.notion.site/image/https%3A%2F%2Fs3-us-west-2.amazonaws.com%2Fsecure.notion-static.com%2F49dabb74-ffff-418a-8a72-26ed2a6c2f72%2FUntitled.png?table=block&id=245bc35e-55d3-468a-9c94-ad0ac25290db&spaceId=a3f51d20-62c5-408a-823f-471ed08ec100&width=1410&userId=&cache=v2" alt="img" title="image Title" />
	<br>
	<img src="https://manssorr.notion.site/image/https%3A%2F%2Fs3-us-west-2.amazonaws.com%2Fsecure.notion-static.com%2Fb8eda863-2846-4823-b24d-5552455bfb15%2FUntitled.png?table=block&id=d500e754-1f34-4b07-b67b-3c246e13003d&spaceId=a3f51d20-62c5-408a-823f-471ed08ec100&width=990&userId=&cache=v2" alt="img" title="image Title">
	<br>
	Now search at them to find duplications and the useless ones
	<img src="https://manssorr.notion.site/image/https%3A%2F%2Fs3-us-west-2.amazonaws.com%2Fsecure.notion-static.com%2F2523c469-56bd-4699-ab20-be0d632f3993%2FUntitled.png?table=block&id=b6e91e7a-0f4d-4175-b497-66ed9ea565fe&spaceId=a3f51d20-62c5-408a-823f-471ed08ec100&width=1480&userId=&cache=v2" alt="img" title="image Title">
</details>
<details>
	<summary><strong>Identifying class relationships</strong></summary>
	Now after pick the class to the conceptual model we need to identify the relations between them with draw lines between them
	<br>
	Once we have the potential objects picked out for our conceptional model, it's useful to indicate the main relationships or associations between those concepts by drawing lines between the boxes.
	<br>
  	Now, optionally, it may be useful to add a short note to actually describe the relationship.
	<br>
	then write down a work which describe the relation between them
	<br>
	The benefit of detailing these relationships is that it makes it easier to realize which objects interact with each other, meaning which objects have behaviors that affect other objects.
	<br>
	<img src="https://manssorr.notion.site/image/https%3A%2F%2Fs3-us-west-2.amazonaws.com%2Fsecure.notion-static.com%2Fc8de4732-2f75-4e01-91dd-dbae99478af4%2FUntitled.png?table=block&id=e6999521-f2a8-4c38-9be2-7af49e9e5e64&spaceId=a3f51d20-62c5-408a-823f-471ed08ec100&width=1130&userId=&cache=v2"  alt="img" title="image Title">
</details>
<details>
	<summary><strong>Identifying class responsibilities</strong></summary>
	Now we need to know each class (object) responsibilities, so we back to use cases and user stories then searching this time for verbs only
	<br>
	We need to figure out the responsibilities for our conceptual objects to really identify what are, and what are not classes that we'll need to create.
	<br>
	We will go back to the user stories and  look for verbs, and verb phrases to identify responsibilities.
	<br>
	<img src="https://manssorr.notion.site/image/https%3A%2F%2Fs3-us-west-2.amazonaws.com%2Fsecure.notion-static.com%2F5dd78045-b45e-4714-815d-4e855a5ebae7%2FUntitled.png?table=block&id=cd0ebe73-edb0-4a3f-a2f5-383d27da213c&spaceId=a3f51d20-62c5-408a-823f-471ed08ec100&width=1390&userId=&cache=v2" alt="img" title="image Title">
	<br>

> An object should be responsible for itself
<br>
	like steers asteroid for first look you may said the player who responsible for steer it !
	<br>
	but no, the player only ask the asteroid to move and the asteroid itself responsible to his move
	<br>
	<img src="https://manssorr.notion.site/image/https%3A%2F%2Fs3-us-west-2.amazonaws.com%2Fsecure.notion-static.com%2F24ce28fb-11d8-4914-b19a-acace07eb252%2FUntitled.png?table=block&id=5c38e419-20af-4607-9940-b5921fcb5027&spaceId=a3f51d20-62c5-408a-823f-471ed08ec100&width=1600&userId=&cache=v2" alt="img" title="image Title">
	<br>
	Don't give much behaviors(responsibilities) to single actor but the mean actor could ask other things to there behaviors
	<img src="https://manssorr.notion.site/image/https%3A%2F%2Fs3-us-west-2.amazonaws.com%2Fsecure.notion-static.com%2F84d1c953-70a3-40cd-94db-b442e9cdd363%2FUntitled.png?table=block&id=59ff3479-8f33-44b3-b0f6-f78e024371a7&spaceId=a3f51d20-62c5-408a-823f-471ed08ec100&width=1510&userId=&cache=v2" alt="img" title="image Title">
	<br>
	System word here refers to some part of the system should do that not an actor called system will do ! to avoid doing that :
	<br>
	<img src="https://manssorr.notion.site/image/https%3A%2F%2Fs3-us-west-2.amazonaws.com%2Fsecure.notion-static.com%2F2fe2a6a7-b3d1-48cc-acdb-79cbf3a0f379%2FUntitled.png?table=block&id=5c6d6a1f-9c0c-4514-aa95-8b977d47c4b8&spaceId=a3f51d20-62c5-408a-823f-471ed08ec100&width=2000&userId=&cache=v2" alt="img" title="image Title">
	<br>
	<img src="https://manssorr.notion.site/image/https%3A%2F%2Fs3-us-west-2.amazonaws.com%2Fsecure.notion-static.com%2F6a0f6d57-09da-474e-a327-ab72358c62c7%2FUntitled.png?table=block&id=b053f382-215a-41d8-87f4-495adf687bde&spaceId=a3f51d20-62c5-408a-823f-471ed08ec100&width=2000&userId=&cache=v2" alt="img" title="image Title">
</details>
<details>
	<summary><strong>CRC Cards</strong></summary>
	<br>
	<strong>CRC: </strong>Class Responsibilities Collaboration
	<br>
	<strong>Each CRC cards represents one class</strong>
	<ul>
		<li>it has three sections. The first section is the name of the class at the top, which is usually underlined.</li>
		<li>The Right section  is the Responsibilities of the class, the things that it needs to take care of.</li>
		<li>The left section  is for the Collaborators, the other classes it interacts with.</li>
	</ul>
	CRC cards typically use this format with the responsibilities taking up the left two-thirds of the card, and the collaborators on what's remaining to the right.
	<br>
	<br>
	<strong>CRH: </strong>Component Responsibilities Helper
	<br>
	It should be like that and on a small piece of paper, to make it simple.
	<br>
	<img src="https://manssorr.notion.site/image/https%3A%2F%2Fs3-us-west-2.amazonaws.com%2Fsecure.notion-static.com%2Ffbef972f-518b-4529-9c17-cd551fba3c36%2FUntitled.png?table=block&id=3455ea55-fc92-410a-ac4b-afca421d8823&spaceId=a3f51d20-62c5-408a-823f-471ed08ec100&width=820&userId=&cache=v2" alt="img" title="image Title">
	<br>
	Use NOUNS to find Class , And VERBS to Responsibilities
	<br>
	<img src="https://manssorr.notion.site/image/https%3A%2F%2Fs3-us-west-2.amazonaws.com%2Fsecure.notion-static.com%2Fd778ae96-578f-44ee-96a0-58a90314ddec%2FUntitled.png?table=block&id=26157f67-2f8d-40a9-b65e-16e33bc79c80&spaceId=a3f51d20-62c5-408a-823f-471ed08ec100&width=830&userId=&cache=v2" alt="img" title="image Title">
</details>
<details>
	<summary><strong>Chalange: Jukebox conceptual model</strong></summary>
	<img src="https://manssorr.notion.site/image/https%3A%2F%2Fs3-us-west-2.amazonaws.com%2Fsecure.notion-static.com%2F50126ae2-6160-4a45-8eda-a07d92aa3b05%2FUntitled.png?table=block&id=649be3cd-debe-4db7-8d97-8582eadb215d&spaceId=a3f51d20-62c5-408a-823f-471ed08ec100&width=1570&userId=&cache=v2">
	<br>
	<img src="https://manssorr.notion.site/image/https%3A%2F%2Fs3-us-west-2.amazonaws.com%2Fsecure.notion-static.com%2F6e8e59f4-a480-44ca-8fd6-0fa825b90305%2FUntitled.png?table=block&id=c3cc288c-5604-4be4-81b9-a75f81ff5e6d&spaceId=a3f51d20-62c5-408a-823f-471ed08ec100&width=1610&userId=&cache=v2">
	<br>
	<img src="https://manssorr.notion.site/image/https%3A%2F%2Fs3-us-west-2.amazonaws.com%2Fsecure.notion-static.com%2F307ea140-1d62-4dfd-9f3f-b27c3856e4c5%2FUntitled.png?table=block&id=3f0b056e-97b5-404e-98ab-d49e4bd9c8ec&spaceId=a3f51d20-62c5-408a-823f-471ed08ec100&width=2000&userId=&cache=v2">
	<br>
	Removing system to Avoiding master class
	<img src="https://manssorr.notion.site/image/https%3A%2F%2Fs3-us-west-2.amazonaws.com%2Fsecure.notion-static.com%2F7097015c-1858-4b00-b102-cbb767b7d6bb%2FUntitled.png?table=block&id=a63c731d-ee06-4d5b-989e-54a6111f998a&spaceId=a3f51d20-62c5-408a-823f-471ed08ec100&width=670&userId=&cache=v2">
	<br>
	<img src="https://manssorr.notion.site/image/https%3A%2F%2Fs3-us-west-2.amazonaws.com%2Fsecure.notion-static.com%2F638d9d26-f738-4e13-9532-b55ec2c2f92b%2FUntitled.png?table=block&id=9faebf58-7cc7-48ff-b629-39c3a65616e2&spaceId=a3f51d20-62c5-408a-823f-471ed08ec100&width=1440&userId=&cache=v2">
	<br>
	<img src="https://manssorr.notion.site/image/https%3A%2F%2Fs3-us-west-2.amazonaws.com%2Fsecure.notion-static.com%2Fa5b1d328-0667-4f0f-84d1-dbd28c9c173f%2FUntitled.png?table=block&id=e3df3e52-264d-44f4-a524-4b3b266c0888&spaceId=a3f51d20-62c5-408a-823f-471ed08ec100&width=2000&userId=&cache=v2">
</details>

### Class Diagrams
<details>
	<summary><strong>Creating class diagrams: Attributes</strong></summary>
	<strong>Class Diagram</strong>
	<br>
	<ul>
		<li><strong>ClassName</strong>: Spaceship</li>
		<li>
			<strong>Attributes</strong>
			<ul>
				<li>callSign</li>
				<li>shieldActive</li>
				<li>shieldStrength</li>
				<li>position</li>
			</ul>
		</li>
		<li>
			<strong>Behaviors</strong>
			<ul>
				<li>getShieldStrength</li>
				<li>reduceShield</li>
				<li>getPosition</li>
				<li>move</li>
				<li>setPosition</li>
			</ul>
		</li>
	</ul>
	<br>
	<br>
	<strong>Behavior</strong>  they're usually named as short verb phrases.
	<br>
	it's common practice to name methods that modify and retrieve attributes as get instant operations rather than things like change or retrieve.
	<br>
  	And some languages will even automatically generate getter and setter methods for you.
	<br>
	<br>
	 You'll commonly see plus and minus signs before the attributes and methods in UML class diagrams.
	<br>
	Which is referred to as controlling visibility.
	<br>
	Minus indicates that a member should be private to the class, meaning it's not directly accessible by other objects.
	<br>
  	plus means the member should be public.
	<br>
	<br>
	The rule here is to leave as many attributes and methods private as possible, and only make something public if you know another object will need to use it.
	<br>
	Your focus should really be on what object do rather than just viewing them as data structures.
</details>
<details>
	<summary><strong>Creating class diagrams: Behaviors</strong></summary>
	At behavior we can use Responsibilities from Conceptional model which we had created Responsibility(Input datatype) : Return datatype
	<br>
	Incapsolation: + Public - Private
	<img src="https://manssorr.notion.site/image/https%3A%2F%2Fs3-us-west-2.amazonaws.com%2Fsecure.notion-static.com%2F4902c992-ece1-43b4-8682-1c6b951e0a90%2FUntitled.png?table=block&id=5f72e7d8-7bd2-48b3-8f22-895401db3da0&spaceId=a3f51d20-62c5-408a-823f-471ed08ec100&width=1120&userId=&cache=v2">

> The rule: to make many as you can every thing is private, and only public if another object will need to use it
</details>
<details>
	<summary><strong>Converting class diagrams into code</strong></summary>

```
	public class Spaceship {

	// instance variables
	public String callsign;
	private int shieldStrength;

	// methods
	public String fireMissile() {
	return "Pew!";
	}

	public void reduceShield(int amount) {
	shieldStrength -= amount;
	}
}
```
<br>
</details>
<details>
	<summary><strong>Instantiating classes</strong></summary>
	To make a new object in different languages:
	<br>
	<img src="https://manssorr.notion.site/image/https%3A%2F%2Fs3-us-west-2.amazonaws.com%2Fsecure.notion-static.com%2Fa8c7c2dd-672b-4d5c-8c94-38e52242e61c%2FUntitled.png?table=block&id=7764beaa-b2db-4700-b0d6-dc21c50b6e70&spaceId=a3f51d20-62c5-408a-823f-471ed08ec100&width=2000&userId=&cache=v2">
	<br>
	<br>
	<strong>Constructor: </strong>A special method that gets called to create an object
	<br>
	It should contain the initial values that i want to be for each new object of this class.
	<br>
	And it should be a method on the class with same name of it and be + <strong>(Public)</strong>
</details>
<details>
	<summary><strong>Class with multiple constructors</strong></summary>
	At this point maybe some one say: What if I need to make an object with different initial values from the one you made the constructor with ? I will reply then make multiple constructors!
	<br>
	<br>
	<strong>Multiple Constructors:</strong> Also called overloading its to let the first constructor take in value at the argument ( ) to make another object with different initial values
	<br>
	most langauges will let us create multiple constructor methods through a process called overloading
	<br>

```
public class Spaceship {

	// instance variables
	public String callSign;
	private Int shieldStrength

	// constructor methods
	public Spaceship() {
		name = "The nameless ship";
		shieldStrength = 100; }

	// overload constructor
	public Spaceship(String name) {
		callSign = name;
		shieldStrength = 200;

	// other methods omitted
}
```
<strong>Method Overloading</strong> Which allow a class to have more than one method with the same name, but different sets of input parameters
	<br>
	Overloading multiple constructors gives us flexibility to pass in information when actually creating object
	<br>
	<br>
	<strong>Destructor</strong> A special method that gets called when the object is destroyed
	<br>
	<strong>Finalizer</strong> A special method that gets called when the object is destroyed
</details>
<details>
	<summary><strong>Static attributes and methods</strong></summary>
	<strong>Instance Variable: </strong>Variable for which each instantiated object of a class has a separate copy
	<br>

```
public class Spaceship {

	// instance variables
	public String callSign;
	private int shieldStrength;

	// class variables
	public static float toughness;

	// other code omitted
}
```
<br>
Just define it inside the class but out side the _ init_ function:
<br>

```
class Spaceship():

	# class variables
	toughness = 0.8

	def _init_(self):

		# instance variables
		self.callsign = "
		self._shieldStrength = 100

	# other code omitted
```
<br>
But to access it we should use className.classVariable NOT just as a normal Var
<br>
<img src="https://manssorr.notion.site/image/https%3A%2F%2Fs3-us-west-2.amazonaws.com%2Fsecure.notion-static.com%2Fb2ac4f90-1911-4938-a3e4-6d3debea0b05%2FUntitled.png?table=block&id=8bd50164-ee0e-4018-abf1-6953be901896&spaceId=a3f51d20-62c5-408a-823f-471ed08ec100&width=1640&userId=&cache=v2">
<br>
	<strong>Static Variable</strong>
	<br>
	<ul>
		<li>Variable that is shared across all objects in a class</li>
		<li>Also called a shared varible or a class variable</li>
	</ul>
	<br>
	At UML Statics member should be Underlined
	<br>
	<img src="https://manssorr.notion.site/image/https%3A%2F%2Fs3-us-west-2.amazonaws.com%2Fsecure.notion-static.com%2Fff77fb17-4a27-4396-a730-c7d78c536e72%2FUntitled.png?table=block&id=38958c1c-7b5d-4649-b52f-212a12dee4f3&spaceId=a3f51d20-62c5-408a-823f-471ed08ec100&width=640&userId=&cache=v2" >
</details>
<details>
	<summary><strong>Challenge: Jukebox class diagrams</strong></summary>
	<img src="https://manssorr.notion.site/image/https%3A%2F%2Fs3-us-west-2.amazonaws.com%2Fsecure.notion-static.com%2F0e827136-1df9-4c4d-8d27-641b29418543%2FUntitled.png?table=block&id=e94baa53-8c58-4e29-a2c3-5bda7a04d54b&spaceId=a3f51d20-62c5-408a-823f-471ed08ec100&width=1600&userId=&cache=v2" >
	<br>
	Here You make vars private so made two public get methods to access them
	<br>
	<img src="https://manssorr.notion.site/image/https%3A%2F%2Fs3-us-west-2.amazonaws.com%2Fsecure.notion-static.com%2F18a1a301-4d2f-4e2a-a1e6-e312cfc919de%2FUntitled.png?table=block&id=e4de6685-fa1e-410d-9391-6a5290d4838d&spaceId=a3f51d20-62c5-408a-823f-471ed08ec100&width=1020&userId=&cache=v2" >
	<br>
	<img src="https://manssorr.notion.site/image/https%3A%2F%2Fs3-us-west-2.amazonaws.com%2Fsecure.notion-static.com%2F488c66d8-18b8-4d07-8650-59f6490abb71%2FUntitled.png?table=block&id=4c66410f-0578-43cc-8f00-656de073e689&spaceId=a3f51d20-62c5-408a-823f-471ed08ec100&width=510&userId=&cache=v2" >
	<br>
	<img src="https://manssorr.notion.site/image/https%3A%2F%2Fs3-us-west-2.amazonaws.com%2Fsecure.notion-static.com%2F842cfe87-ebbe-4ef4-9cba-29db9b79b6aa%2FUntitled.png?table=block&id=6556c625-b78e-4801-880d-cb8d417e49d8&spaceId=a3f51d20-62c5-408a-823f-471ed08ec100&width=500&userId=&cache=v2" >
	<br>
	<img src="https://manssorr.notion.site/image/https%3A%2F%2Fs3-us-west-2.amazonaws.com%2Fsecure.notion-static.com%2F6338b670-0d9f-462d-bef8-1e09abdbef2a%2FUntitled.png?table=block&id=ed3b1843-05b8-4e32-b167-fb1073d2e0f7&spaceId=a3f51d20-62c5-408a-823f-471ed08ec100&width=2000&userId=&cache=v2" >
</details>

### Inheritance	and Composition
<details>
	<summary><strong>Identifying inheritance situations</strong></summary>
	<strong>inheritance:</strong> subclasses or child classes automatically have all of the attributes and methods of their parent class. And they can have their own unique attributes and methods in addition to those.
	<br>
	<br>
	The best way to identify if it's inheritance, is with two simple words, is a (a kind of , or  type of ) Inheritance describes an is a relationship between objects.
	<br>
	Like: A star fighter is a spaceship, or A cargo shuttle is a spaceship.
	<br>
	<img src="https://manssorr.notion.site/image/https%3A%2F%2Fs3-us-west-2.amazonaws.com%2Fsecure.notion-static.com%2Fa3e1db4c-a866-443d-bc73-1bd8b2210436%2FUntitled.png?table=block&id=d86b1594-f74a-4194-bdb0-8630c6ba4797&spaceId=a3f51d20-62c5-408a-823f-471ed08ec100&width=2000&userId=&cache=v2">
	<img src="https://manssorr.notion.site/image/https%3A%2F%2Fs3-us-west-2.amazonaws.com%2Fsecure.notion-static.com%2Fef963b1c-0f93-430b-8323-fb1bc6b9a4d9%2FUntitled.png?table=block&id=35e1eedc-13a2-48fa-9864-08b6f656108b&spaceId=a3f51d20-62c5-408a-823f-471ed08ec100&width=1140&userId=&cache=v2">
	<br>
	<br>
	<strong>Overriding:</strong> Allowing a subclass to replace the implementation of a method from the superclass
	<br>
	<strong>Method Overriding:</strong>is change one or more methods from the superClass with the same name to take the same input but change the function itself.
	<br>
	<br>
	And you can make a multilevel Inheritance

> It's Normal to didn't use any inheritance on every diagram you make!
</details>
<details>
	<summary><strong>Using inheritance</strong></summary>
	At different languages:
	<img src="https://manssorr.notion.site/image/https%3A%2F%2Fs3-us-west-2.amazonaws.com%2Fsecure.notion-static.com%2F8c48b3c0-6a88-4d16-b704-e7b8e176def8%2FUntitled.png?table=block&id=4f14896a-eca6-4a38-b6f6-daa428998370&spaceId=a3f51d20-62c5-408a-823f-471ed08ec100&width=2000&userId=&cache=v2">
	<br>
	To calling a method from the super class you may use the keyword Super like that:
	<img src="https://manssorr.notion.site/image/https%3A%2F%2Fs3-us-west-2.amazonaws.com%2Fsecure.notion-static.com%2Fad910232-1961-4058-8a35-1f573188e7c7%2FUntitled.png?table=block&id=130e2284-0ac5-43d9-92a0-c0371405b2c9&spaceId=a3f51d20-62c5-408a-823f-471ed08ec100&width=2000&userId=&cache=v2">
</details>
<details>
	<summary><strong>Abstract and concrete classes</strong></summary>
	<ul>
		<li>
			<details>
				<summary><strong>Abstract from GeeksForGeeks.Org</strong></summary>
				<strong>C++:</strong>  Sometimes implementation of all function cannot be provided in a base class because we don’t know the implementation. Such a class is called abstract class. For example, let Shape be a base class. We cannot provide implementation of function draw() in Shape, but we know every derived class must have implementation of draw(). Similarly an Animal class doesn’t have implementation of move() (assuming that all animals move), but all animals must know how to move. We cannot create objects of abstract classes.
				<br>
				<br>
				<strong>Java: </strong> An abstract class that is declared by the abstract keyword. An abstract class cannot be instantiated directly, i.e. the object of such class cannot be created directly using the new keyword. An abstract class can be instantiated either by a concrete subclass or by defining all the abstract method along with the new statement. It may or may not contain an abstract method. An abstract method is declared by abstract keyword, such methods cannot have a body. If a class contains an abstract method, then it also needs to be abstract.
			</details>
		</li>
		<li>
			<details>
				<summary><strong>Concrete from GeeksForGeeks.Org</strong></summary>
				<strong>Java: </strong>A concrete class in Java is a type of subclass, which implements all the abstract method of its super abstract class which it extends to. It also has implementations of all methods of interfaces it implements.
			</details>
		</li>
		<li>
			<details>
				<summary><strong>Important points (Java)</strong></summary>
				<ul>
					<li>A concrete class is a subclass of an abstract class, which implements all its abstract method.</li>
					<li>Abstract methods cannot have body.</li>
					<li>Abstract class can have static fields and static method, like other classes.</li>
					<li>An abstract class cannot be declared as final.</li>
					<li>Only abstract class can have abstract methods.</li>
					<li>A private, final, static method cannot be abstract, as it cannot be overridden in a subclass.</li>
					<li>Abstract class cannot have abstract constructors.</li>
					<li>Abstract class cannot have abstract static methods.</li>
					<li>If a class extends an abstract class, then it should define all the abstract methods (override) of the base abstract class. If not, the subclass(the class extending abstract class) must also be defined as abstract class.</li>
				</ul>
			</details>
		</li>
	</ul>
	<br>
	<strong>Abstract Class:</strong>
	<ul>
		<li>it's exists to be inherited by other classes</li>
		<li>Cannot be instantiated</li>
		<li>should contains at least one abstract method</li>
		<li>And not all of his methods should be abstract some of them can be implemented</li>
	</ul>
	<br>

> The benefit of including keywords like abstract and final is to communicate your intentions for a class to other programmers. It let's them know whether or not a class was designed with inheritance in mind.
</details>
<details>
	<summary><strong>Interfaces</strong></summary>
	<strong>Interface: </strong>
	<ul>
		<li>(is a form of abstraction) it list of methods for a class to implement.</li>
		<li>It doesn't contain any actual behavior.</li>
		<li>you're not allowed to put any functionality inside an interface.</li>
	</ul>
	<br>
	A class can implement multiple interfaces.
	<br>
	<br>
	Different between Interface and Abstract Class:
	<ul>
		<li>Interface represent a <strong>capability, that class implements</strong></li>
		<li>Abstract represent a <strong>type, that another class can inherit from.</strong></li>
	</ul>
	<br>
	The Implementation of interface at UML:
	<br>
	<img src="https://manssorr.notion.site/image/https%3A%2F%2Fs3-us-west-2.amazonaws.com%2Fsecure.notion-static.com%2F787c517a-0539-49a0-bd65-b9acf53a38ca%2FUntitled.png?table=block&id=91804cb2-93e4-4c08-bf97-054062977962&spaceId=a3f51d20-62c5-408a-823f-471ed08ec100&width=1060&userId=&cache=v2">
	<br>
	<br>

> Program to an interface, not to an implementation.

	because it's a developer's choice how to implement those methods rather than being provided with that code
</details>
<details>
	<summary><strong>Aggregation</strong></summary>
	<strong>Aggregation: </strong>is often referred to as a <strong>has a(has Many or Uses a or Uses Many) </strong> relationship like: the road has cars.
	<br>
	"Has a" relation ship  OR " Uses a" or "Uses many"
	<br>
	<br>
	UML is:
	<br>
	<img src="https://manssorr.notion.site/image/https%3A%2F%2Fs3-us-west-2.amazonaws.com%2Fsecure.notion-static.com%2F2f01611c-fdb5-4d7b-b669-8f84fd2a5809%2FUntitled.png?table=block&id=a1afc56c-ef68-479f-abdb-f3851098cbed&spaceId=a3f51d20-62c5-408a-823f-471ed08ec100&width=710&userId=&cache=v2">
</details>
<details>
	<summary><strong>Composition</strong></summary>
	<strong>Composition: (Is a more specific form of aggregation): </strong>Like aggregation, composition is based around a has-a relationship between objects but it specifically implies ownership so i say owns a(n) . Like: the spaceship owns the engine.
	<br>
	the owned element has no meaning or purpose with out the owner element, like the engine if I destroys the spaceship the engine would be destroyed too !
	<br>
	<br>
	SO. When you creating a class which will has a <strong>Composition</strong> relation take care of <strong>constructor and destructor</strong>
	<br>
	UML is:
	<br>
	<img src="https://manssorr.notion.site/image/https%3A%2F%2Fs3-us-west-2.amazonaws.com%2Fsecure.notion-static.com%2F383f0c1f-9a8d-4f86-b364-57f317c343ed%2FUntitled.png?table=block&id=07beb4d4-62d4-4a25-b525-317c4bfaceb0&spaceId=a3f51d20-62c5-408a-823f-471ed08ec100&width=2000&userId=&cache=v2">
</details>
<details>
	<summary><strong>Challenge: Jukebox class relationships</strong></summary>
	<img src="https://manssorr.notion.site/image/https%3A%2F%2Fs3-us-west-2.amazonaws.com%2Fsecure.notion-static.com%2Fcc6ed069-9b68-4277-978c-e4ccb5e0693a%2FUntitled.png?table=block&id=e9169960-f86a-4725-965a-e56ef7f47d97&spaceId=a3f51d20-62c5-408a-823f-471ed08ec100&width=2000&userId=&cache=v2">
	<br>
	<img src="https://manssorr.notion.site/image/https%3A%2F%2Fs3-us-west-2.amazonaws.com%2Fsecure.notion-static.com%2Fefedbb04-118c-4285-87af-cad1d4aaf629%2FUntitled.png?table=block&id=9d8d0844-1a4e-4e0f-b298-dd5bc054f58f&spaceId=a3f51d20-62c5-408a-823f-471ed08ec100&width=2000&userId=&cache=v2">
	<br>
	<img src="https://manssorr.notion.site/image/https%3A%2F%2Fs3-us-west-2.amazonaws.com%2Fsecure.notion-static.com%2F849d5f1f-853f-4aaa-82d9-1e526fe1efca%2FUntitled.png?table=block&id=bf735e94-1f9e-4119-aa7a-3cf2b9ab9ce0&spaceId=a3f51d20-62c5-408a-823f-471ed08ec100&width=2000&userId=&cache=v2">
</details>

### Software Development
<details>
	<summary><strong>OOP support in different languages</strong></summary>
	Typing = The data type of variables when declaration
	<br>
	<img src="https://manssorr.notion.site/image/https%3A%2F%2Fs3-us-west-2.amazonaws.com%2Fsecure.notion-static.com%2Fe27539a8-e8b8-46a2-91bd-7780868e4e09%2FUntitled.png?table=block&id=82e2007d-7336-42f5-9e50-3f783f500069&spaceId=a3f51d20-62c5-408a-823f-471ed08ec100&width=2000&userId=&cache=v2">
</details>
<details>
	<summary><strong>General development principles</strong></summary>
	<strong>SOLID</strong>
	<ul>
		<li><strong>Single responsibility principle:</strong> A class should have only a single responsibility</li>
		<li>Open/closed principle</li>
		<li>Liskov substitution priciple</li>
		<li>Interface segregation priciple</li>
		<li>Dependency inversion priciple</li>
	</ul>
	<br>
	<strong>DRY:</strong> Don't Repeat Yourself
	<br>
	<strong>YAGNI:</strong> You Ain't Gonna Need it
	<br>
	<strong>Code Smell:</strong> Any characteristic in a program's code that possibly indicates a deeper problem

</details>
<details>
	<summary><strong>Software testing</strong></summary>
	<strong>Documentation</strong> getting starter guides and training are all good and can help make a basic user become a power user
	<br>
	The software should be easy and intuitive to use
</details>
<details>
	<summary><strong>Design patterns</strong></summary>
	<strong>Design Pattern:</strong> The re-usable form of a solution to a design problem
	<br>
	<br>
	<strong>Factory Method Pattern:</strong> which could provide a structured way to instantiate different types of enemy spaceships based on the current level and difficulty setting.
	<br>
	<img src="https://manssorr.notion.site/image/https%3A%2F%2Fs3-us-west-2.amazonaws.com%2Fsecure.notion-static.com%2Fb05c860d-7058-41c7-b9db-7852167559ae%2FUntitled.png?table=block&id=0dcdac64-be81-4ebe-a665-84d3d4e18a86&spaceId=a3f51d20-62c5-408a-823f-471ed08ec100&width=2000&userId=&cache=v2">
	<br>
	<br>
	<strong>Memento design pattern:</strong> which outlines a proven approach for restoring an object to a previous state.
	<br>
	<img src="https://manssorr.notion.site/image/https%3A%2F%2Fs3-us-west-2.amazonaws.com%2Fsecure.notion-static.com%2F1e46edf5-25be-467d-83f0-40941a6278f6%2FUntitled.png?table=block&id=3f8572c9-d1d5-4d02-bc8f-1434f72ddc39&spaceId=a3f51d20-62c5-408a-823f-471ed08ec100&width=2000&userId=&cache=v2">
	<br>
	<br>
	<ul>
		<li>
			<strong>Creational patterns:</strong> focused on the instantiation of objects and provide clever ways to have more flexibility in how object are actually created
			<br>
			<img src="https://manssorr.notion.site/image/https%3A%2F%2Fs3-us-west-2.amazonaws.com%2Fsecure.notion-static.com%2F3e236516-b0d4-4990-8896-be977731dcc9%2FUntitled.png?table=block&id=06909e78-2741-4948-919c-d32a9bf609fb&spaceId=a3f51d20-62c5-408a-823f-471ed08ec100&width=340&userId=&cache=v2">
		</li>
		<li>
			<strong>structural patterns:</strong> describe how classes are actually designed. How things like inheritance and composition and aggregation can be used to provide extra functionality.
			<br>
			<img src="https://manssorr.notion.site/image/https%3A%2F%2Fs3-us-west-2.amazonaws.com%2Fsecure.notion-static.com%2F724c3888-af86-4832-b431-c9de54679741%2FUntitled.png?table=block&id=8185625f-0ed4-43cd-8cd6-e1ea28a5c193&spaceId=a3f51d20-62c5-408a-823f-471ed08ec100&width=240&userId=&cache=v2">
		</li>
		<li>
			<strong>behavioral patterns:</strong> are specifically concerned with the communication between objects as a program is running
			<br>
			<img src="https://manssorr.notion.site/image/https%3A%2F%2Fs3-us-west-2.amazonaws.com%2Fsecure.notion-static.com%2F724c3888-af86-4832-b431-c9de54679741%2FUntitled.png?table=block&id=8185625f-0ed4-43cd-8cd6-e1ea28a5c193&spaceId=a3f51d20-62c5-408a-823f-471ed08ec100&width=240&userId=&cache=v2">
		</li>
	</ul>
	<br>
	<br>
	<strong>Some recommended books</strong>
	<ul>
		<li>Design patterns: Elements of Reusable object-oriented</li>
		<li>Head First Design Patters: A Brain-Friendly Guide</li>
	</ul>
</details>
