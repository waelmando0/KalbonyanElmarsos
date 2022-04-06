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
		<strong>Class: </strong>is a template for the object
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
        Hiding unnecessary details and functionalities and only showing what is important to work is an abstraction.
        <br>
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
<details>
		<summary><strong>Quiz</strong></summary>
		<strong>What is the difference between object-oriented programming and procedural programming?</strong>
		<br>
		Procedural programming specifies a sequence of tasks, but object-oriented programming describes the properties of tools or items.
		<br>
		In object-oriented programming, there are some elements of procedural programming in the description of objects.
		<br>
	  <br>
		<strong>How does dynamic polymorphism differ from static polymorphism?</strong>
		<br>
		It uses overriding instead of overloading.
		<br>
		Dynamic polymorphism creates a unique instance.
		<br>
		<br>
		<strong>What is overriding a method?</strong>
		<br>
		Creating a unique version of an inherited method.
		<br>
		<br>
		<strong>How are analysis and design different?</strong>
		<br>
		Analysis describes a problem; design describes a solution.
		<br>
		<br>
		<strong>What is the term for a visual representation of the classes in an application?</strong>
		<br>
		class diagram
		<br>
		<br>
		<strong>In addition to attributes and methods, what does a UML class diagram contain?</strong>
		<br>
		the class name
		<br>
		<br>
		<strong>How do object behaviors and attributes differ?</strong>
		<br>
		Attributes describe a state, but behaviors describe actions.
		<br>
		<br>
		<strong>You are designing a traffic simulation program. What is a possible attribute that you could use for a car object?</strong>
		<br>
			 gas mileage
		<br>
		<br>
		<strong>Shonzu has gathered the requirements for a new solution, described the application he is going to build, and identified the main objects in the solution. What should he do next?</strong>
		<br>
		Describe object interactions.
		<br>
		This will be essential for understanding behaviors.
		<br>
		<br>
		<strong>What is the purpose of encapsulation?</strong>
		<br>
		to protect an object from unwanted changes
		<br>
		<br>
		<strong>In addition to attributes and behaviors, which quality must a class posses</strong>
		<br>
		a name
		<br>
		<br>
		<strong>In the following class diagram, what does lower() represent?</strong>

```
TRIPOD
height
width
angle
raise()
lower()
point()
fold()
```
a behavior
<br>
		Behaviors come at the end of a class diagram, and contain room for arguments.
		<br>
		<br>
		<strong>What is a benefit of using a programming language that has a large library?</strong>
		<br>
		Many classes are already defined and can be used without have to re-define them.
		<br>
		<br>
		<strong>In the following class diagram, what does height represent?</strong>
		<br>

```
TRIPOD
height
width
angle
raise()
lower()
point()
fold()
```
an attribute
<br>
	Attributes are generally nouns, and are placed just below the title.
	<br>
	<br>
	<strong>We're using abstraction when we define a(n) _____.</strong>
	<br>
	class
	<br>
	<br>
	<strong>Focusing on the idea of a person instead of an individual is an example of what fundamental idea in object-oriented programming?</strong>
	<br>
	abstraction
	<br>
	<br>
	<strong>Steve is able to turn on and adjust his television even though he does not know how it works internally. This exemplifies which principle of object-oriented programming?</strong>
	<br>
	encapsulation
	<br>
	<br>
	<strong>Why is inheritance used when creating a new class?</strong>
	<br>
	to avoid redefining attributes and behaviors
	<br>
	<br>
	<strong>If an attribute is added to a superclass, what happens to all of the objects of the subclass?</strong>
	<br>
	Each subclass object automatically receives the additional attribute.
	<br>
	<br>
	<strong>Static polymorphism uses method _____.</strong>
	<br>
	overloading
</details>

### Requirements
<details>
		<summary><strong>Defining Requirements</strong></summary>
		<strong>Requirements</strong> = What does it need to do?
		<br>
		<br>
		<strong>Funcational Requirements:</strong> = What must it do?
		<br>
		The system must:
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
		<strong>FURPS</strong>
		<ul>
			<li>
				<strong>Functionality: </strong>Capability, Reusability, Security
				<br>
				the Features of the app
			</li>
			<br>
			<li>
				<strong>Usability: </strong>Human Factors, Aesthetics, Consistency, Documentation
				<br>
				what affect the person who will use the app? Is it easy on the eyes?
			</li>
			<br>
			<li>
				<strong>Reliability: </strong>Availability, Failure Rate & Duration, Predictability
				<br>
				How Much system downtime is acceptable? Is system can be recovered?
			</li>
			<br>
			<li>
				<strong>Performance: </strong>Speed, Efficiency, Resource, Consumption, Scalability
			</li>
			<br>
			<li>
				<strong>Supportability: </strong>Testability, Extensibility, Serviceability, Configurability
			</li>
		</ul>
		<br>
		<strong>FURPS+</strong>
		<ul>
			<li><strong>Design: </strong>constraints on how the application is built.</li>
			<li><strong>Implementation: </strong>the language in which the application is built</li>
			<li><strong>Interface: </strong>Communication with other devices is a common need.</li>
			<li><strong>Physical: </strong>the hardware on which the application must run.</li>
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
<details>
	<summary><strong>Quiz</strong></summary>
	<strong>What is the first step in defining requirements for an application?</strong>
	<br>
	determining what the application must have and do
	<br>
	<br>
	<strong>Which is a valid nonfunctional requirement?</strong>
	<br>
	The system should be updated annually.
	<br>
	<br>
	<strong>A requirement that all onscreen text must be at least 20-point font size is an example of which FURPS quality?</strong>
	<br>
	usability
	<br>
	<br>
	<strong>In which category does extensibility of an application reside?</strong>
	<br>
	supportability
	<br>
	<br>
	<strong>Atul is working on an application that must communicate with a scientific instrument and a data archiving system. Into which category would these requirements fall in the FURPS+ model?</strong>
	<br>
	interface: Communication with other devices is a common need.
</details>

### Use Cases and User Stories
<details>
	<summary><strong>Use cases</strong></summary>
	<ul>
		<li><strong>Title: </strong>What is the goal?</li>
		<li><strong>Primary Actor: </strong>Who desires it?</li>
		<li><strong>Success Scenario: </strong>How is it accomplished?</li>
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
	Thinking about another systems or organizations which need to connect with your system. (Systems = Box)
</details>
<details>
	<summary><strong>Identifying the scenarios</strong></summary>
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

<details>
	<summary><strong>Quiz</strong></summary>
	<strong>When creating a use case diagram, what can you do to show each self-contained use case?</strong>
	<br>
	draw an ellipse around each use case
	<br>
	<br>
	<strong>What is wrong with the following scenario description. "The pedals were used to control speed and direction."</strong>
	<br>
	It is passive and focuses on means instead of intent.
	<br>
	<br>
	<strong>What is the function of a use case diagram?</strong>
	<br>
	It connects actors to use cases.
	<br>
	<br>
	<strong>Why are arrows and numbers not found in use case diagrams?</strong>
	<br>
	Sequence and direction are not critical at this stage.
	<br>
	Listing features and their connectivity is the function of a use case diagram.
	<br>
	<br>
	<strong>What is typically written on index cards, and describes a small scenario from a user perspective?</strong>
	<br>
	user story
	<br>
	<br>
	<strong>User stories are _____ than use cases.</strong>
	<br>
	shorter and less detailed
	<br>
	<br>
	<strong>Marge is working on a short and simple project involving inventory maintenance. Why should she write short use cases?</strong>
	<br>
	They help identify problems but do not create the confusing work of full use cases.
	<br>
	Casual use cases can be very helpful, but the use cases should be more fully developed for larger projects.
	<br>
	<br>
	<strong>Which sentence is most appropriate for a use case scenario?</strong>
	<br>
	User adjusts contrast and brightness controls.
	<br>
	<br>
	<strong>What is the role of the primary actor in a use case?</strong>
	<br>
	to interact with the application to achieve the goal
	<br>
	<br>
	<strong>When are fully fleshed out cases most appropriate?</strong>
	<br>
	for large, complex projects
	<br>
	<br>
	<strong>You are creating a use case for an application that controls the dispensing of gasoline at a pump. Who is the primary actor in this scenario?</strong>
	<br>
	the customer who uses the pump
	<br>
	<br>
	<strong>What distinguishes primary actors?</strong>
	<br>
	What distinguishes primary actors?
</details>

### Domain Modeling

<details>
	<summary><strong>Identifying the objects</strong></summary>
	<strong>Conseptual Model: </strong> Represents important objects and the relationships between them
	<br>
	This model is done after analysis phase (Use cases & user stories)
	<br>
	at this point we pick all our system objects and every thing we should be aware of
	<br>
	To get the objects we go back to the use cases and the user stories then pick all of the nouns
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
	then write down a work which describe the relation between them
	<br>
	<img src="https://manssorr.notion.site/image/https%3A%2F%2Fs3-us-west-2.amazonaws.com%2Fsecure.notion-static.com%2Fc8de4732-2f75-4e01-91dd-dbae99478af4%2FUntitled.png?table=block&id=e6999521-f2a8-4c38-9be2-7af49e9e5e64&spaceId=a3f51d20-62c5-408a-823f-471ed08ec100&width=1130&userId=&cache=v2"  alt="img" title="image Title">
</details>
<details>
	<summary><strong>Identifying class responsibilities</strong></summary>
	Now we need to know each class (object) responsibilities, so we back to use cases and user stories then searching this time for verbs only
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
<details>
	<summary><strong>Quiz</strong></summary>
	<strong>How can one avoid assigning too many responsibilities to a single object?</strong>
	<br>
	Require objects to take care of themselves to a greater extent.
	<br>
	<br>
	<strong>What common problem should new programmers avoid when designing a program?</strong>
	<br>
	creating a god object
	<br>
	<br>
	<strong>In addition to responsibilities, which should be listed on CRC cards?</strong>
	<br>
	interacting classes
	<br>
	<br>
	<strong>Which design tool contains the same information as a conceptual object diagram?</strong>
	<br>
	CRC cards
	<br>
	<br>
	<strong>After analysis and use cases are completed, what is the first step in the design phase of a project</strong>
	<br>
	creating a conceptual model
	<br>
	<br>
	<strong>When is there a relationship between two objects?</strong>
	<br>
	when one object depends on or affects the other object
	<br>
	<br>
	<strong>When diagramming relationships between objects, what is the UML notation that represents one or more objects?</strong>
	<br>
	 1…*
	<br>
	<br>
	<strong>How can you identify candidates for objects?</strong>
	<br>
	by listing all of the nouns in the user stories
	<br>
	Objects are nouns; they are things.
	<br>
	<br>
	<strong>Which words in the following list are candidates for objects: trumpet, clean, enrage, leaf, tree, collapse, active, or lively?</strong>
	<br>
	trumpet, leaf, and tree
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
<details>
	<summary><strong>Quiz</strong></summary>
	<strong>In which language is the following class specification written?</strong>

```
class Dog():
      def __init__(self):
#instance variables
      self.breed=""
       self.weight=50
#methods
```
Python
<br>
Python does not use curly braces nor terminal semicolons.
	<br>
	<br>
	<strong>Instantiating a class in many languages looks similar to that in C++, DinnerPlate *myPlate = new DinnerPlate(). What is the main difference between Python and Swift for achieving the same goal?
	</strong>
	<br>
	the absence of the word new
	<br>
	Swift uses `let`, but neither Swift nor Python use `new`.
	<br>
	<br>
	<strong>A class Dog has the following constructors:</strong>
	<br>

```
public Dog()
public Dog(String breed)
public Dog(int weight)
```
How would you instantiate a Dog with the weight set in Java?
<br>
	Dog Fido = new Dog(63);
	<br>
	The dog's weight is set to 63.
	<br>
	<br>
	<strong>Which languages require the use of static to declare class-wide variables or methods?</strong>
	<br>
	Java and C#
	<br>
	The word `static` can be confusing, because it implies that there is only one instance.
	<br>
	<br>
	<strong>Which class diagram correctly specifies data types and default values?</strong>
	<br>

```
Asteroid
size: Integer=5
position: Coordinate=(0.5,0.5,0.6)
velocity: Coordinate=(1,0,0)
```
It helps to have standard syntax even in UML, as it makes later jobs easier.
<br>
	<br>
	<strong>Which is the function of a finalizer or destructor?</strong>
	<br>
	to relinquish resources that are no longer needed
	<br>
	<br>
	<strong>How would you declare a class variable in Ruby named maxScore?</strong>
	<br>
	@@maxScore
	<br>
	<br>
	<strong>A class diagram contains the following behavior specifications. Which data type is returned by the accelerate() behavior?</strong>
	<br>

```
move(Direction)
accelerate(Acceleration): Velocity
setPosition(Coordinate)
explodePieces(Integer)
```
Velocity
<br>
	The return data type is indicated after the colon.
	<br>
	<br>
	<strong>A class diagram contains the following behavior specifications. The explodePieces() behavior breaks up an object into a number of pieces. What is the data type for that number? The answer will take the place of the '???'.</strong>
	<br>

```
move(Direction)
accelerate(Acceleration): Velocity
setPosition(Coordinate)
explodePieces(???)
```
Integer
<br>
	An argument is contained within parentheses.
	<br>
	<br>
	<strong>For which case would the use of a static attribute be appropriate?</strong>
	<br>
	the weather conditions for each house in a small neighborhood
	<br>
	<br>
	<strong>In which language would you find the following declaration of an instance variable?</strong>
	<br>

``private var _size: Int``
<br>
	Swift
	<br>
	The use of `var` is unique.
	<br>
	<br>
	<strong>What other terminology is used for variables that are declared static?</strong>
	<br>
	class or shared
	<br>
	<br>
	<strong>What does the value (0.5,0.5,0.5) indicate in the class diagram specification position: Coordinate = (0.5,0.5,0.5)?</strong>
	<br>
	a default value of the position attribute
	<br>
	<br>
	<strong>In a UML class diagram, how would you write an attribute called Name that is a String data type and has a default value of Jane?</strong>
	<br>
	Name: String = "Jane"
	<br>
	<br>
	<strong>In the class diagram specification setSize(Integer):Integer, to what do the integer specifications refer?</strong>
	<br>
	the data types for the argument, and return of the function setSize
	<br>
	<br>
	<strong>Which line of Java code declares a public method called getName that accepts no arguments and returns a String value?</strong>
	<br>
	public String getName()
	<br>
	<br>
	<strong>Which line of Java code will instantiate a new object named Student from the Person class?</strong>
	<br>
	Person Student = new Person()
	<br>
	<br>
	<strong>Which is the purpose of a constructor?</strong>
	<br>
	to initialize attribute values
	<br>
	<br>
	<strong>The class Person has the following constructors:</strong>
	<br>

```
public Person()
public Person(String name)
public Person(int age)
```
Which one will be called when a new person is created with the following command?
<br>

``Person Steve = new Person(39)``
<br>
	Person(int age)
	<br>
	<br>
	<strong>Which restrictions apply to the use of static methods?</strong>
	<br>
	They cannot act on instance variables, but only static variables.
	<br>
	Static methods can be applied to class-wide variables.
	<br>
	<br>
	<strong>What does it mean if a class attribute is private?</strong>
	<br>
	It can only be accessed from within the class.
	<br>
	<br>
	<strong>How do you declare a private variable in Python?</strong>
	<br>
	Python does not have private or public variables.
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
	<strong>Interface: </strong>(is a form of abstraction) it list of methods for a class to implement. It doesn't contain any actual behavior.
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
<details>
	<summary><strong>Quiz</strong></summary>
	<strong>Which relationship is a good candidate for superclass and subclass?</strong>
	<br>
	utensil-fork
	<br>
	<br>
	<strong>What does this line of Java code declare?</strong>

```
public class Apple extends Fruit {
```
a new class Apple that is inherited from the class Fruit
<br>
	<br>
	<strong>Why is the syntax for inheritance in C++ different from most other languages?</strong>
	<br>
	because a class can inherit from multiple levels in C++
	<br>
	<br>
	<strong>Which line of code will define a C# abstract class named School?</strong>
	<br>
	abstract class School {
	<br>
	<br>
	<strong>Which concept of object-oriented programming is displayed by using the "is a kind of" comparison between 2 classes?</strong>
	<br>
	inheritance
	<br>
	<br>
	<strong>A concrete class has no _____.</strong>
	<br>
	children
	<br>
	<br>
	<strong>Why would you create an abstract class, if it can have no real instances?</strong>
	<br>
	to avoid redundant coding in child classes
	<br>
	<br>
	<strong>An aggregation is a _____.</strong>
	<br>
	collection of objects
	<br>
	<br>
	<strong>What form of aggregation implies ownership, and that the lifetime of an object is dependent on another object's existence?</strong>
	<br>
	composition
	<br>
	<br>
	<strong>How are the contents of a composition different from those of an aggregation?</strong>
	<br>
	If a composition dies, the contents die.
	<br>
	<br>
	<strong>In Java, how would you define an interface named Box that contains two methods named Open and Close that don't accept or return any variables?</strong>
	<br>

```
	interface Box {
	void Open();
	void Close();
```
<br>
	<strong>What do most languages have in common for referring to a method defined in the parent class?</strong>
	<br>
	the use of super in the prefix to the method name
	<br>
	The word `super` is used for the common need for code within a subclass, to call a method that was originally defined in the super class.
	<br>
	<br>
	<strong>Why should you use abstract and final in class definitions?</strong>
	<br>
	to better communicate intentions
	<br>
	Their use makes the code easier to read and maintain.
	<br>
	<br>
	<strong>When is an interface used instead of an abstract class?</strong>
	<br>
	when you need to describe the capabilities of a class
	<br>
	<br>
	<strong>Which relationship between classes is referred to as a "has a" relationship?</strong>
	<br>
	aggregation
	<br>
	<br>
	<strong>Which representation is correct UML for the interface Edible?</strong>
	<br>

```
<<interface>>
Edible
beEaten()
```
We represent an interface using a box that looks similar to a class, and include a tag with double angle quotes to indicate an interface.
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