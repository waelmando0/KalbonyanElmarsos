## Programming Foundation: Beyond the fundamentals

### Collections
<details>
	<summary><strong>Understand Collections</strong></summary>
	<strong>collection</strong>: Grouping multiple items together and storing them with a single name, called a variable
	By using a collection, the very structure of your code is indicating that multiple pieces of data are related.
	<br>
    <strong>The advantages of using collections</strong>
	<br>
	<ul>
		<li>Uses your code structure to indicate that multiple pieces of data are related</li>
		<li>Avoids creating a potentially huge number of variables to track within our code</li>
		<li>Offers simplified syntax</li>
	</ul>
	<br>
	<strong>types:</strong>
        <ul>
            <li>1.Dectionarys</li>
            <li>2.Lists</li>
        </ul>
    <br>
	<strong>dictionary</strong>: A dictionary is enclosed in curly braces, and includes a tag name for each value. ( Associative array - Map - Table )
	<br>
	<strong>List</strong>: Simple collection that groups pieces of data together in a certain order and assigns the collection a name
	To create a list, you enclose the value in square brackets, and then for the collection, provide values separated by commas.
    <br>
	# List items in python can be any type of data
	it's similar Array in Javascript but
	<br>
</details>
<details>
	<summary><strong>Creating Collections Example</strong></summary>

```
# the first kind of collection is the list
# this is the syntax

friends = ["wes", "kait", "snnekers"]

country1 = [
    'egypt',
    'syria',
    'palestine',
    'turkey',
]

country2 = [
    'turkey',
    'spain',
    'germany',
    'brazil',

```

```
# the second kind of the collection is the dictionary or the hash table
# each for each item there is a key or label and a value
# key  :  value

california_symbols = {
    'bird': 'California quail',
    'animal': 'Grizzly bear',
    'flower': 'California poppy',
    'fruit': 'Avocado',
}
```
</details>
<details>
	<summary><strong>Collections in other languages</strong></summary>
    in Python, each item in a list can be of any data type.
    <br>
    So you could combine strings, numbers, and other types of data like Boolean values, all in the same list.
    <br>
    But other languages, like C++, require that all values in this type of collection must be of the same data type.for instance, containing all strings or all numbers, but no combination of these or other types of data
    <br>
    <br>
	<strong>Mutable</strong>
	meaning that we can be changed the value of item existing
    <br>
	<strong>Immutable</strong>
	meaning that we cannot changed the value of item existing
	<br>
	<br>
	in the python there are a collection known as a tuple
	<br>
	<strong>Tuple</strong>
	An immutable list
</details>
<details>
	<summary><strong>Challange: Working with a collection</strong></summary>

```
peaks = [
    'African': 'Kilimanjaro',
    'Antarctic': 'Vinson',
    'Australian': 'Punncak Jaya',
    'Eurasian': 'Everest',
    'North_American': 'Denali',
    'Pacific': 'Mauna Kea',
    'South_American': 'Aconcagua',
]

print(peaks[Pancific])
```
</details>


### Iteration
<details>
	<summary><strong>Introduction Iteration</strong></summary>
	<strong>Iteration</strong>: Repeats the same produce multiple times until it reaches a specified endpoint
	<br>
	<strong>Loop</strong>: Code that iterates, moving from beginning to end of the process, then starting over
	<br>
	<br>
	<strong>to write code that iterates!! you commonly need a few specific pices of information</strong>
	<ul>
		<li>Specify the data</li>
		<li>What should happen to the data during each iteration</li>
		<li>Indicate when the loop should stop</li>
	</ul>
	<br>
	<strong>Infinite Loop</strong>
	Bug that can occur when the ending condition is omitted or specified incorrectly
</details>
<details>
	<summary><strong>Iterating through collections</strong></summary>
	<strong>For</strong>: Specifies a variable name that we can use in each iteration of the loop to reference the current value
	<br>
	<strong>In</strong>: Indicates that what follows is the set of values that we want to iterate through
	<br>
    <strong>End point:</strong> When I iterate at list of items and didn't make an end point for the loop, It will ends with last item in the list
	<br>

```
spices = [
    'salt',
    'pepper',
    'cumin',
    'turmeric'
]

for spice in spices:
    print(spice)
```
</details>
<details>
	<summary><strong>Iterating to a custom endpoint</strong></summary>
    <br>
	<strong>While:</strong> is the iteration loop with step and condition

```
i = 0
print("I will count to 200 by tens:")
while i <= 200:
        print(i)
        i += 10
print("we're do it!!")
```
</details>

<details>
	<summary><strong>Challenge: creating a for loop</strong></summary>

```
fruits = [
    'apples',
    'bananas',
    'dragon fruit',
    'mangos',
    'nectarines',
    'pears'
]

print("our fruit selection:")
for fruit in fruits:
    print(fruit)
```
</details>

### External code
<details>
	<summary><strong>Comparing types of external code</strong></summary>
	<strong>Module:</strong> Python file that contains code, like variables or functions.
    <br>
    <br>
    <strong>Library\Package:</strong> Using multiple modules together so they are distributed and used in a group.
    <br>
    <br>
	<strong>Framework:</strong> when a set of code is not just used together but used in a specific way.
</details>

<details>
	<summary><strong>Working with a module</strong></summary>
	<strong>first of all we should import it </strong>

```
import testmodule
testmodule.mult(10,20)
```

> The Module file should be in the same directory of the code which will be used in.
<br>
<strong>Test Module:</strong>

```
def mult(x, y):
    print(f'{x} * {y} = {x * y}')
```
</details>

<details>
	<summary><strong>Understanding libraries and frameworks</strong></summary>
	<strong>Python libraries:</strong>
	<ul>
		<li>TensorFlow</li>
		<li>pandas</li>
		<li>NumPy</li>
		<li>SciPy</li>
	</ul>
	<strong>Python Frameworks:</strong>
	<ul>
		<li>Django</li>
		<li>Flask</li>
	</ul>
	<br>
	<strong>Javascript libraries:</strong>
	<ul>
		<li>Lodash</li>
		<li>jQuery</li>
	</ul>
	<strong>Javascript Frameworks:</strong>
	<ul>
		<li>Angular</li>
		<li>React</li>
		<li>Vue</li>
	</ul>
	<br>
</details>

### Working with strings
<details>
	<summary><strong>Combining and manipulating strings</strong></summary>
	<strong>Concatenation:</strong> When multiple strings are combined into a single string.
	<br>
	<strong>String:</strong> is a box can hold any type of data char, int, symbol
</details>
<details>
	<summary><strong>Finding patterns in strings</strong></summary>
	<strong>Slicing</strong>: Getting part of a string value
	<br>
	<strong>capitalize()</strong> Method of Capitalize the first Char of word
	<br>
	<br>
	<strong>Finding text Methods</strong>
	<ul>
		<li>find() </li>
		<li>index()</li>
		<li>rfind</li>
		<li>rindex</li>
	</ul>
</details>
<details>
	<summary><strong>Creating regular expressions</strong></summary>
    <strong>Regular Expression (Regex):</strong>Allow  you to create a description of a pattern that you want to match (Letters, Numbers, Special Characters)
    <br>
    Regular expression is basically used to describe a pattern of characters so it's used for pattern matching or pattern searching, commonly used for validation, as well as, pulling things out of a body of text, or body of characters, email addresses, phone number social security numbers things that have certain patterns in their formatting

<br>
<strong>Brackets [] - Character Sets</strong>

* i      => Case Insensitive
* g      => Global Search
* m      => Multi Line Search
* eh     => Brackets Character | Must be between eh
* ^eh    => Brackets Not Character | Match anything expect eh
* a-e    => Match any lowercase Letters
* A-E    => Match any uppercase Letters
* A-Zz-a => Match any letter
* 0-9    => Range Number | Match any digit
* ^0-9   => Not Range Number | Match anything digit expect
* A-g    => Range [A-Z] Range[a-z]
* 0-9a-z => Double Range


<strong>Shorthand Character Classes</strong>

* \w   =>   Word Character (a-z, A-Z, 0-9, _)
* \W   =>   Not a Word Character.
* \w+  =>   + = one or more
* \d   =>   Any Digits (0-9)
* \D   =>   Not a Digit (0-9)
* \d+  =>   Match any digit 0 or more time
* \s   =>   Spaces of any kind. (space, tab, new line)
* \S   =>   It is not a Space, Tab or new line.
</details>
<details>
	<summary><strong>Challenge: Strings</strong></summary>

```
miles = input('Enter a distance in miles: ')
# kilometers_value = miles_value * 1.609344

miles_float = float(miles)
km = ( miles * 1.609344 )
print ("The distance is ",km , "kilometers")
print (km)
```
</details>

### Planning a Program
<details>
	<summary><strong>Choosing a code style</strong></summary>
    <strong>Style Guide:</strong> Documentation on approaches to code
    <br>
    Popular Style guide of Python is:
    <br>
    * PEP8.
    <br>
    * Google.
    <br>
    <br>
    and for JavaScript for example we have <strong>Airbnb</strong> Style guide.
</details>
<details>
	<summary><strong>Writing pseudocode</strong></summary>
    <strong>Pseudocode :</strong> writing a description of what you're trying to do using plain language
    <br>
    Pseudo coding helps you create a basic outline of the program you're creating
    <br>
    Pseudo code  frees you from having to decide on a specific syntax to use or even a specific language. Instead, you simply describe what you need to accomplish.
    <br>
    When your pseudo code is done, you're left with an outline for your program, which you can then built out using a programming language.

```
check if the user has entered a number
	if no
display a message asking the user to enter a number
	if yes
calculate the square root of the number
	display the result
```
<br>
<strong>Example:</strong>

```
number = 0
if number == 0 :
    number = int(input("Please Enter a number: "))
    print("The square root of",number, "is: ",number * number)
else:
    print("The square root of",number, "is: ",number * number)
```

</details>

### Input and Output
<details>
    <summary><strong>Introduction to input and output</strong></summary>
    <ul>
        <li>Study your project before starting write a single line of code</li>
        <li>Select language and technologies you will use and the scope of you work</li>
        <li>Then finally define the inputs/outputs of you project what will be like!</li>
    </ul>
</details>
<!--
<details>
    <summary><strong>Working with file input and output</strong></summary>
    > python excute → Solve the file error
    <strong>open() </strong>: opens a file, and returns it as a file object, it takes two parameters;
    <ul>
        <li>filename </li>
        <li>mode</li>
    </ul>
    There are four different methods (modes) for opening a file:
    <ul>
        <li>`r` - Read   - Default value. Opens a file for reading, error if the file does not exist</li>
        <li>`a` - Append - Opens a file for appending, creates the file if it does not exist</li>
        <li>`w` - Write  - Opens a file for writing, creates the file if it does not exist</li>
        <li>`x` - Create - Creates the specified file, returns an error if the file exists</li>
    </ul>
    <br>
    In addition you can specify if the file should be handled as binary or text mode
    <ul>
        <li>`t` - Text   - Default value. Text mode</li>
        <li>`b` - Binary - Binary mode (e.g. images)</li>
    </ul>
</details>
-->

### Debugging
<details>
    <summary><strong>Introduction to debugging</strong></summary>
    <strong>Debugging :</strong> Identifying and fixing bugs
    <span>Types of bugs</span>
    <ul>
        <li><strong>Syntax Error :</strong> Code doesn't match the rules of the language</li>
        <li><strong>Run-Time Error :</strong> Calling function doesn't defined yet, the calling syntax is right but the function is not exist</li>
        <li><strong>Logix Error :</strong> Loop counting is the wrong direction it will be got into infinite loop error</li>
    </ul>

```
i = 10
while i > 0:
	i += 1 # the error here it will be counting for ever!
print(i)
```
</details>
<details>
    <summary><strong>Creating a test case</strong></summary>
    Test Cases: Commands or scripts designed to test a specific scenario

<strong>Example</strong>

```
# at the code grade

def check_grade(mark):
    if mark > 90:
        print("Grade: O")
    elif mark >= 80 and mark < 90:
        print("Grade: A+")
    elif mark >= 70 and mark < 80:
        print("Grade: A")
    elif mark >= 60 and mark < 70:
        print("Grade: B+")
    elif mark >= 50 and mark < 60:
        print("Grade: B")
    elif mark >= 40 and mark < 50:
        print("Grade: C")
    else:
        print("Grade: F")

check_grade(45)
check_grade(75)
check_grade(89)
check_grade(99)
```
</details>
</details>
<details>
    <summary><strong>Challenge: Debugging</strong></summary>

```
def plant_recommendation(care):
    # Syntax Error
    if care == 'low':
        print('aloe')
    elif care == 'medium':
        print('pothos')
    # Logic Error
    elif care == 'high':
        print('orchid')

# Runtime Error
plant_recommendation('low')
plant_recommendation('medium')
plant_recommendation('high')
```
</details>


### Object Orientation
<details>
    <summary><strong>Introduction to object-Oriented programming</strong></summary>
    <strong>What are they?</strong>
    <br>
    Well objects allow us to group togather properties and values, or key and values is often what we call it. have many uses from storing related data, from storing functionality
    <br>
    <br>
    <strong>OOP:</strong> Breaks the program to smaller parts called objects, Each on has focused purpose, they communicate together to make the program functions.
    <br>
    <br>
    Each object has
    <ul>
        <li>Attributes (The data of the object): <strong>Properties</strong></li>
        <li>Behaviors  (What the object can do): <strong>Methods</strong></li>
    </ul>
    <br>
    <strong>The main Object called CLASS:</strong> You can make class for each type of object, and make unlimited number objects from it with same pattern but contain different properties values
</details>
<details>
    <summary><strong>Using built-in classes</strong></summary>
    <strong>For Example</strong>
    <br>

```
flips = [
    'heads',
    'tails',
    'tails',
    'heads',
    'tails',
]

print(flips.count(heads))
print(flips.pop())
```
</details>
<details>
    <summary><strong>Creating custom classes and objects</strong></summary>

```
class Attendee:
    'Common base class for all attendees'

    def __init__(self, name, tickets):
        self.name = name
        self.tickets = tickets

    def displayAttendee(self):
        if self.tickets == 0:
            print('Name : {}, Tickets: {}'.format(self.name, "Kick Him !!"))
        else:
            print('Name : {}, Tickets: {}'.format(self.name, self.tickets))

    def addTicket(self):
        self.tickets += 1
        print('{} tickets increased to {}'.format(self.name, self.tickets))

    def delTicket(self):
        if self.tickets >= 1:
            self.tickets -= 1
            print('{} tickets decreased to {}'.format(self.name, self.tickets))
        else:
            print("You can't make it -Ve MAN >_< !!")

Attendee1 = Attendee('Mansour Ashraf', 2)
Attendee2 = Attendee('Ahmed Mansour', 2)
Attendee3 = Attendee('T. Hosney', 5)

Attendee1.displayAttendee()
Attendee2.displayAttendee()
Attendee3.displayAttendee()

Attendee1.addTicket()
Attendee1.addTicket()
Attendee1.addTicket()

Attendee3.delTicket()
Attendee3.delTicket()
Attendee3.delTicket()

Attendee2.delTicket()
Attendee2.delTicket()
Attendee2.delTicket()

Attendee1.displayAttendee()
Attendee2.displayAttendee()
Attendee3.displayAttendee()
```
</details>

### Advanced Topics
<details>
    <summary><strong>Memory management across languages</strong></summary>
    <strong>Computer Storage</strong>
    <ul>
        <li>
            <strong>Drive</strong>
            <ul>
                <li>Programs</li>
                <li>Data</li>
            </ul>
        </li>
        <li>
            <strong>Memmory</strong>
            <ul>
                <li>Running Code</li>
                <li>Results</li>
            </ul>
        </li>
    </ul>
    <br>
    <strong>Memory Management: </strong> Code that decides what's kept in memory and what's thrown away
    <br>
    <strong>Garbage Collection: </strong> An automated memory management process that keeps track of which items aren't needed and deletes them.
    <ul>
        <li>Python</li>
        <li>Javascript</li>
        <li>Ruby support it</li>
    </ul>
</details>
<details>
    <summary><strong>Introduction to multithreading</strong></summary>
    <strong>Multithreading:</strong> is code structured as separated tasks that are executed simultaneously.
    <br>
    Each task called thread and requires additional processing power and memory
    <br>
    Multithreading is not asynchronous code but it's very similar.
</details>
<details>
    <summary><strong>Introduction to algorithms</strong></summary>
    <strong>Algorithm:</strong> A set of instructions to describe the exact result
</details>
