## Programming Foundations: Data Structures

### Introduction to Data Structures
<details>
    <summary><strong>Introduction to data and data types</strong></summary>
    <strong>Data Type:</strong> An attribute of data that describes the values it can have and how the data can be used
    <br>
    <br>
    Data is information that is stored or processed by a computer
    <br>
    <strong>Common Types of Data</strong>
    <br>
    <ul>
        <li>Numbers</li>
        <li>Letters</li>
        <li>True (1)</li>
        <li>False (0)</li>
    </ul>
</details>
<details>
    <summary><strong>Numerical data type</strong></summary>
    <strong>Two Types</strong>
    <ul>
        <li><strong>whole numbers: </strong>short - long - int</li>
        <li><strong>decimal numbers: </strong>double - float</li>
    </ul>
    <br>
    <strong>what the difference between each of these data types?</strong>
    <br>
    is the precision with which they store their values, in other words, <strong>the difference is the range of numerical values that data type can store.</strong>
    <br>
    <br>
    <strong>Whole Numbers</strong>
    <table>
        <tr>
            <td> Short </td>
            <td> -32,768 to 32,767 </td>
            <td> 64 bits </td>
        </tr>
        <tr>
            <td> Int </td>
            <td> ~-3 billion to ~2 billion </td>
            <td> 32 bits </td>
        </tr>
            <tr>
            <td> Long </td>
            <td> -(2) to 2 </td>
            <td> 64 bits </td>
        </tr>
    </table>
    <br>
    <strong>decimal Numbers</strong>
    <table>
    <tr>
        <td> Float </td>
        <td> ~7 decimal digits </td>
        <td> 32 bits </td>
    </tr>
    <tr>
        <td> Double </td>
        <td> ~16 decimal digits </td>
        <td> 64 bits </td>
    </tr>
    </table>
    <br>
    <br>
    <strong>few examples of what storing various numbers</strong>
    <table>
        <tr>
            <td>Floats in Java</td>
            <td>float x = 10.0f;</td>
        </tr>
        <tr>
            <td>Numbers in Javascript</td>
            <td>var myNum = 29</td>
        </tr>
        <tr>
            <td>Doubles in Swift</td>
            <td>var myNum:Double = 10.24</td>
        </tr>
    </table>
</details>
<details>
    <summary><strong>Boolean and Characters</strong></summary>
    A Boolean is a true or false value.
    <br>
    <strong>Boolean in C#:</strong>
    <br>
    bool isLightOn = false;
    <br>
    <br>
    <strong>Boolean in Python:</strong>
    <br>
    isLightOn = true;
    <br>
    <br>
    <strong>A character in c++:</strong>
    <br>
    char firstInitial = 'K';
    <br>
    <br>
    <strong>A character in Kotlin:</strong>
    <br>
    val firstInitial: char = 'K';
    <br>
    <br>
    <ul>
        <li>C++ the char takes (8 bits)</li>
        <li>Kotlin the char takes (16 bits)</li>
    </ul>
</details>
<details>
    <summary><strong>Primitive types in memory</strong></summary>
    <strong>Primitive Types</strong>
    <br>
    <ul>
        <li>ints</li>
        <li>doubles</li>
        <li>longs</li>
        <li>floats</li>
        <li>shorts</li>
        <li>booleans</li>
        <li>chars</li>
    </ul>
</details>
<details>
    <summary><strong>Introduction to data structures</strong></summary>
    <strong>Data Structures:</strong> are containers they allow us to combine several pieces of data into a single structure
    <br>
    <br>
    <strong>Why use a data structure?</strong>
    <br>
    we could have created individual variables for every student and store the appropriate number of pets each student has in each variable
    <br>
    <ul>
        <li>int numberOfPetsForStudent1 = 0;</li>
        <li>int numberOfPetsForStudent2 = 1;</li>
        <li>int numberOfPetsForStudent3 = 0;</li>
    </ul>
    <br>
    when we try to do anything with that data like compute the average number of pets each student has or try to find out which value is most common <strong>it will be very difficult because the variables are not linked in any way</strong>
    <br>
    <strong>So we need data structures because they help us connect and group our data</strong>
    <br>
    <br>
    Different data structures are not only desiged to organize and store data to suit a specific purpose but also give a way to access and work with that data in an efficient manner
    <br>

> Data structures give us organization storage and access
</details>
<details>
    <summary><strong>Strings</strong></summary>
    <strong>String</strong> is a sequence of characters it's data type that's buit out of another data type
    <br>
    <br>
    <strong>String in javascript:</strong>
    <br>
    var name = "Jessican"
    <br>
    <br>
    <strong>String in Python:</strong>
    <br>
    name = 'Jessica'
    <br>
    <br>
    <strong>What Exact Size of Data Structure Depends On</strong>
    <ul>
        <li>Allocated space for structure</li>
        <li>Number of pieces of data</li>
        <li>Size of each data piece</li>
    </ul>
</details>
<details>
    <summary><strong>Primitive vs. Reference types in memory</strong></summary>
    primitive types that take up a specific amount of bits
    <br>
    <br>
    Data structures are different because the amount of space they take up often depends on how they are allocated, initialized and maintained
    <br>
    <br>
    <strong>Referenced Types (variableName -> memoryAddress -> value)</strong>
    <br>
    <ul>
        <li>Strings</li>
        <li>Data structures</li>
    </ul>
    <br>
    <strong>Primitive Types (variableName -> data)</strong>
    <br>
    <ul>
        <li>int</li>
        <li>boolean</li>
        <li>character</li>
        <li>float</li>
        <li>double</li>
        <li>short</li>
        <li>long</li>
    </ul>
    <br>
    Each Programming language determines what access you have to memory management tools
    <br>
    C++ (manage pointers, memory, and data)
</details>
<details>
    <summary><strong>Quiz</strong></summary>
    <strong>How do referenced types differ from primitive types?</strong>
    <br>
    Referenced types use pointers to addresses.
    <br>
    <br>
    <strong>Why do programmers use data structures rather than individual values?</strong>
    <br>
    for ease of access
    <br>
    <br>
    <strong>Which data type only uses one bit per instance?</strong>
    <br>
    Boolean
    <br>
    <br>
    <strong>Which data type uses the most storage per value?</strong>
    <br>
    long
</details>

### Arrays
<details>
    <summary><strong>What are Arrays?</strong></summary>
    <strong>Array:</strong> Collection of elements, where each item is identified by an index or key
    <br>
    <strong>Data Structure:</strong>A Collection with a defined way of accessing and storing items
</details>
<details>
    <summary><strong>Use Array in Swift</strong></summary>

```
var perStudentPetCount = [0, 1, 2, 3, 0, 2, 6, 2, 3, 1, 2, 3, 4, 0, 1, 2, 1, 0]
var numOfStudent = perStudentPetCount.count


print(perStudentPetCount[2])
// print(perStudentPetCount[200])
print(numOfStudent)


// for loop example
var sum = 0
for individualPetCount in perStudentPetCount {
    sum = sum + individualPetCount
}
print(sum)


var average = sum / numOfStudent
print(average)
```
</details>
<details>
    <summary><strong>Multidimentional arrays</strong></summary>
    <br>
    with multidimentional array we can add the diemension of a column
    <br>
    <strong>Appetizers:</strong> Salad - Soup - Cheese Plate
    <br>
    <strong>Main Courses:</strong> Chicken - Salmon - Lasagna
    <br>
    <br>
    <table>
        <tr>
            <td>(0,0)</td>
            <td>(0,1)</td>
            <td>(0,2)</td>
        </tr>
        <tr>
            <td>(1,0)</td>
            <td>(1,1)</td>
            <td>(1,2)</td>
        </tr>
    </table>
</details>
<details>
    <summary><strong>Multidimentional arrays in javascript</strong></summary>

```
const dinnerChoices = [
    ["salad", "soup", "cheese plate"],
    ["Chicken", "Salmon", "Lasagna"],
]

let appIndex = 0
let mainDishIndex = 1

const firstApp = dinnerChoices[appIndex][0]
const secondApp =  dinnerChoices[appIndex][1]
const thirdMainDish = dinnerChoices[mainDishIndex][2]

console.log(firstApp)
console.log(secondApp)
console.log(thirdMainDish)

dinnerChoices[mainDishIndex][0] = "steak"
console.log(dinnerChoices[mainDishIndex][0])


console.log(dinnerChoices)
```
</details>
<details>
    <summary><strong>Jagged arrays</strong></summary>
    A jagged array can have elements of different dimensions and sizes
</details>
<details>
    <summary><strong>Jagged arrays in C#</strong></summary>

```
using System;

class Program
{
    static void Main()
    {
        int[][] jagged = new int[3][];

        // set row 0
        jagged[0] = new int[2];
        jagged[0][0] = 8;
        jagged[0][1] = 10;

        // set row 1
        jagged[1] = new int[9];

        // set row 2
        jagged[2] = new int[4] {20, 30, 40, 50};

        Console.WriteLine("At row, col 0: " + jagged[2][0]);
        Console.WriteLine("At row, col 0: " + jagged[2][3]);

    }
}
```
</details>
<details>
    <summary><strong>Resizable arrays and language support</strong></summary>
    <strong>Java, C++</strong>
    <br>
    Basic arrays cannot be resized
    <br>
    <br>
    <strong>Ruby, Javascript</strong>
    <br>
    Basic arrays can be resized
    <br>
    <br>
    <strong>Java</strong>
    <br>
    <ul>
        <li><strong>Immutable:</strong> basic array data</li>
        <li><strong>Mutable:</strong> java classes give us resizable versions</li>
        <li><strong>ArrayList:</strong> comes with extra functionality</li>
    </ul>
    <br>
    <br>
    <strong>ArrayList and Data</strong>
    <br>
    <ul>
        <li>An arrayList is an array under the surface</li>
        <li>Fouce less on maintaining data structures and more on creating</li>
    </ul>
    <br>
    myArrayList.add(2, 10) --> insert the value 10 at index 2
    <br>
    <br>
    <strong>Add, push</strong> Adding to the back of the array
    <br>
    <strong>Remove, pop</strong> Removing from the back of the array
    <br>
    <br>
    <strong>Insert Functionality in Non-mutable Arrays</strong>
    <br>
    <table>
        <tr>
            <td><strong>Basic array in big enough</strong></td>
            <td><strong>Basic array is not big enough</strong></td>
        </tr>
        <tr>
            <td>Items are shuffeld down and new item is added</td>
            <td>All contents copied into a new, bigger basic array, and new items are also copied over with it</td>
        </tr>
    </table>
</details>
<details>
    <summary><strong>Search arrays</strong></summary>
    <strong>Input:</strong> object
    <br>
    <strong>Output:</strong> true/flase value or index
    <br>
    <br>
    <strong>How can we search?</strong>
    <br>
    <ul>
        <li>Check every item</li>
        <li>if match, return true</li>
        <li>If no match (after searching the entire structure), return false</li>
    </ul>
    <br>
    <strong>Example: Java</strong>
    <br>

```
Linear Search / Brute Force soultion in java
for (int i = 0; i < array.length; i++) {
    if item == array[i]{
        return true;
    }
    return false;
}
```
<br>
    <br>
    <strong>Array Search Reminders</strong>
    <br>
    <ul>
        <li>Linear search occurs behind the scences</li>
        <li>indexOf has no information about your data</li>
        <li>Check every element</li>
    </ul>
</details>
<details>
    <summary><strong>Sort arrays</strong></summary>
    <strong>Sorting with Programming Language</strong>
    <br>
    <ul>
        <li>Call sorting function to your collection of object</li>
    </ul>
</details>
<details>
    <summary><strong>Big O notation</strong></summary>
    <strong>Big O Notation</strong> Notation used to describe the performance or complexity of an algorithm
    <br>
    <br>
    <strong>Operations</strong>
    <br>
    <ul>
        <li>Access</li>
        <li>Updated</li>
        <li>Insert</li>
        <li>Search</li>
        <li>Delete</li>
        <li>Sort</li>
    </ul>
    <br>
    <strong>O(1) Time</strong>
    <br>
    <ul>
        <li>Consisitent duraiton of algorithm execution in same time (or space) regardless of the size of the input </li>
        <li>Also called "constant time"</li>
    </ul>
    <br>
    <strong>Outcomes: Insertion</strong>
    <br>
    Best-case-scenario --> Large enough array --> O(1) time (Constant time)
    <br>
    Worst-case-scenario --> Array is full --> O(n) time (linear time)
    <br>
    <br>
    <strong>Outcomes: Search</strong>
    <br>
    Best-case-scenario --> Compare to item --> O(1) time (Constant time)
    <br>
    Worst-case-scenario --> item does not exist --> O(n) time (linear time)
    <br>
    <br>
    <strong>Outcomes: Deletion</strong>
    <br>
    Best-case-scenario --> Locate and delete item --> O(1) time (Constant time)
    <br>
    Worst-case-scenario --> Search, then locate then delete item--> O(n) time (linear time)
    <br>
    <br>
    <strong>Sorting</strong>
    <br>
    <ul>
        <li>Insetion sort</li>
        <li>Merge sort</li>
        <li>Heap sort</li>
        <li>Bubble sort</li>
        <li>Bucket sort</li>
        <li>Radix sort</li>
    </ul>
</details>
<details>
    <summary><strong>Quiz</strong></summary>
    <strong>What is the output of the following JavaScript code?</strong>
    <br>

```
var Salutations = [["Dear", "Hello", "Howdy"], ["Friend", "Judy", "Concerned", "Good Old Pal"]]
console.log(Salutations[1][1])
```
Judy
    <br>
    <br>
    <strong>How many elements are there in a two-dimensional array with length (4,7)?</strong>
    <br>
    28
    <br>
    <br>
    <strong>What is the output of the following Swift code?</strong>
    <br>

```
var noKeys = [5,4,7,8,10,22]
var noChains=noKeys.count
print(noChains)
```
6
    <br>
    <br>
    <strong>Why is a linear search slow?</strong>
    <br>
    It tests every element.
    <br>
    <br>
    <strong>Why should you exercise restraint and care in the use of mutable arrays?</strong>
    <br>
    Their use can slow down performance dramatically.
    <br>
    <br>
    <strong>What is the output of the following C# code?</strong>
    <br>

```
using System;
class Program
{
    static void Main() {
       int[][] jagged = new int[3][];
       jagged[0]=new int[4];
       jagged[1] = new int[2];
       jagged[2]=new int[7];
       Console.WriteLine(jagged[1][1]);
}}
```
0
    <br>
    <br>
    <strong>What is the defining characteristic of a jagged, two-dimensional  array?</strong>
    <br>
    The length in the second dimension is variable.
    <br>
    <br>
    <strong>What is the time complexity for a linear search if the value is not present?</strong>
    <br>
    O(n)
    <br>
    <br>
    <strong>How are data elements referenced in an array?</strong>
    <br>
    with an index or key
</details>

### Lists
<details>
    <summary><strong>Operations on linked lists</strong></summary>
    <ul>
        <li>Add</li>
        <li>Access</li>
        <li>Delete</li>
        <li>Search</li>
    </ul>
</details>
<details>
    <summary><strong>Build a linked list in java</strong></summary>

```
// Linked List
public class LinkedListFromScratch {
    Node head;

    public void add(int data) {
        // LL is empty
        if (this.head == null){
            this.head = new Node(data);
        } else {
        // LL is not empty
            Node nodeToAdd = new Node(data);
            nodeToAdd.next = this.head;
            this.head = nodeToAdd;
        }
    }

    public static void main(String[] args) {
        LinkedListFromScratch myList = new LinkedListFromScratch();
        myList.add(10);
        myList.add(18);
        System.out.println(myList.head.data);
        System.out.println(myList.head.next.data);
    }
}

// Node
class Node {
    int data;
    Node next;

    Node(int d) {this.data = d; }
}
```
</details>
<details>
    <summary><strong>Use linked lists in java</strong></summary>

```
import java.util.LinkedList;

public class MyClass {
    public static void main(String args[]) {
        LinkedList travelBucketList = new LinkedList();

        // Add Items
        travelBucketList.add("santorini, Greece");
        travelBucketList.addFirst("Barcelona, Spain");
        travelBucketList.addLast("Tokyo, Japan");
        travelBucketList.add(2, "Galapagos Islands, Ecuador");
        System.out.println(travelBucketList);

        // Access
        System.out.println(travelBucketList.get(2));
        System.out.println(travelBucketList.getFirst());


        System.out.println(travelBucketList.contains("Barcelona, Spain"));

        // Remove Items
        travelBucketList.removeFirst();
        travelBucketList.removeLast();
        System.out.println(travelBucketList);

        travelBucketList.remove("santorini, Greece");
        travelBucketList.remove(0);
        System.out.println(travelBucketList);

    }
}
```
</details>
<details>
    <summary><strong>Singly vs. doubly Linked lists</strong></summary>
    <strong>Singly Linked</strong> they only have a pointer pointing to the next node in the list. with only a next pointer you can only traverse forward through a list you cannot go backwards
    <br>
    <strong>doubly Linked</strong> we have a next and previous pointer and we can go through the list forward or backward
</details>
<details>
    <summary><strong>Lists in other languages</strong></summary>
    <strong>Java</strong>
    <br>
    <strong>java.util package</strong>
    <br>
    <ul>
        <strong>List interface</strong>
        <li>ArrayList class</li>
        <li>LinkedList class</li>
    </ul>
    <br>
    <br>
    <strong>ArrayList</strong>
    <br>
    <ul>
        <li>Has behavior of a list on the surface</li>
        <li>Stored as an array under the hood</li>
    </ul>
    <br>
    <br>
    <strong>C#</strong>
    <br>
    <ul>
        <strong>Systems.Collections</strong>
        <li>LinkedList</li>
    </ul>
    <br>
    <br>
    No built-in linked lists for swift, Ruby, and javascript
    <br>
    <br>
    <strong>Python</strong>
    <br>
    <ul>
        <li>Lists are resible arrays</li>
        <li>No built-in linked list implementaion</li>
    </ul>
</details>
<details>
    <summary><strong>Quiz</strong></summary>
    <strong>What is returned by MyList.contains("Buy glue") if you are using java.util.LinkedList?</strong>
    <br>
    a Boolean
    <br>
    <br>
    <strong>Where does the following Java code add a new element to a linked list?</strong>
    <br>

```
Node nodeToAdd = new Node(data);
nodeToAdd.next = this.head;
this.head = nodeToAdd;
```
at the head of the list
    <br>
    <br>
    <strong>What is the time complexity for insertion into a linked list?</strong>
    <br>
    O(1)
    <br>
    <br>
    <strong>How does Python implement linked lists?</strong>
    <br>
    as arrays
    <br>
    <br>
    <strong>What is required to change a singly linked list to a doubly linked list?</strong>
    <br>
    a tail node and pointers to previous nodes
    <br>
    <br>
    <strong>You have just added a new element at the end of an existing linked list. What is in the pointer of that new element?</strong>
    <br>
    a null value
    <br>
    <br>
    <strong>What is contained in a node of a linked list?</strong>
    <br>
    data and a pointer
</details>

### Stacks and Queues
<details>
    <summary><strong>What are stacks</strong></summary>
    <strong>Stacks</strong> is an ordered series of objects just like a list but its intended use is slightly different we push objectives on to the stack and pop objects off of it
    <br>
    <strong>(LIFO)</strong> Last in, First out
</details>
<details>
    <summary><strong>Implement stacks in swift</strong></summary>
    <strong>How do stacks work in code?</strong>
    <br>
    Stacks are essentially an ordered list with a specific wat of adding and removing items you can only add and remove from the top
</details>
<details>
    <summary><strong>Use stacks in swift for LIFO</strong></summary>

```
class Stack {
    var stackArray = [String]()

    // Push
    func push(item:String) {
        self.stackArray.append(item)
    }

    // Pop
    func pop()->String? {
        if self.stackArray.last != nil {
            let lastString = self.stackArray.last
            self.stackArray.removeLast()
            return lastString!
        } else {
            return nil
        }
    }

    // Peek
    func peek() -> String? {
        if self.stackArray.last != nil {
            return self.stackArray.last
        } else {
            return nil
        }
    }
}


var deck:Stack = Stack()

deck.push(item: "Heart : Queen")
deck.push(item: "Spade : Jake")
deck.push(item: "Heart : 9")
deck.push(item: "Diamond : 4")
print(deck.peek()!)
print(deck.peek()!)

var firstItemPopped = deck.pop()
var secondItemPopped = deck.pop()
print(firstItemPopped!)
print(secondItemPopped!)
```

</details>
<details>
    <summary><strong>Error tracing with stacks</strong></summary>
    <strong>Runtime stack keeps track of variables</strong> you currently have acces to and what subroutine or function you are in, whenever you get an error, an error message coming from the runtime stack usually appears and <strong>you can retrace your steps and find the error in your code</strong>
    <br>

```
import java.util.Stack;
public class MyClass {
    public static void main(String args[]){
        Stack myStack = new Stack();
        myStack.push("hi");
        myStack.pop();
        myStack.pop();
    }
}
```
</details>
<details>
    <summary><strong>What are queues?</strong></summary>
    <strong>Queues</strong> it is designed to have elements inserted at the end of the queue and elements removed from the beginning of the queue
    <br>
    <strong>Enqueue</strong> is when an item is added to a list
    <br>
    <strong>Dequeue</strong> is when an item is removed from the list
</details>
<details>
    <summary><strong>Implement queues in swift</strong></summary>
    <strong>Stack Functionality</strong>
    <ul>
        <li>Use the tools from the language</li>
        <li>Decide how the queue is implemented</li>
        <li>implement your own</li>
    </ul>
</details>
<details>
    <summary><strong>Use queues in swift for FlFO</strong></summary>

```
class Queue {
    var queueArray = [String]()

    // enqueue
    func enqueue(item:String) {
        self.queueArray.append(item)
    }

    // Pop
    func dequeue()->String? {
        if self.queueArray.first != nil {
            let firstString = self.queueArray.first
            self.queueArray.removeFirst()
            return firstString!
        } else {
            return nil
        }
    }

    // peek
    func peek() -> String? {
        if self.queueArray.first != nil {
            return self.queueArray.first
        } else {
            return nil
        }
    }
}


var myQueue = Queue()
myQueue.enqueue(item: "peggy")
myQueue.enqueue(item: "Larry")
myQueue.enqueue(item: "Serena")

print(myQueue.peek()!)
print(myQueue.peek()!)
var firstToLeave = myQueue.dequeue()
print(myQueue.peek()!)
```
</details>
<details>
    <summary><strong>Queues in other languages</strong></summary>
    <strong>C#</strong>
    <br>
    <ul>
        <li>Enqueue and dequeue</li>
    </ul>
    <br>
    <strong>Python</strong>
    <br>
    <ul>
        <li>put()</li>
        <li>get()</li>
    </ul>
    <br>
    <strong>Ruby and Javascript</strong>
    <br>
    <ul>
        <li>Dynamic arrays</li>
    </ul>
    <strong>C++</strong>
    <br>
    <ul>
        <li>push_back</li>
        <li>pop_front</li>
    </ul>
    <br>
</details>
<details>
    <summary><strong>Specialized queues</strong></summary>
    <strong>Priority Queue</strong> Each element has a priority associated with it
    <br>
    Java has priority queues
    <br>
    C++ has a priority container
    <br>
    <storng>D-E-Q-U-E-K -> Double-ended queue</storng> is like having a stack and a queue at the same time
    <br>
    Items can be added or removed from either end
    <br>
    <br>
    <strong>D-E-Q-U-E-K vs. DEQUEUE</strong>
    <br>
    <ul>
        <li>DEQUEK is a noun</li>
        <li>DEQUEUE is a verb</li>
    </ul>
    <br>
    <strong>D-E-Q-U-E-K Implementaion</strong>
    <br>
    <ul>
        <li>Java has an interface</li>
        <li>C++ has a container</li>
        <li>Python has a class</li>
        <li>No option in Ruby or .NET, but you can use linked lists or dynamic arrays as alternatives</li>
    </ul>
</details>
<details>
    <summary><strong>Pros and cons of stacks and queues</strong></summary>
    <strong>What Stack Are Great For</strong>
    <br>
    <ul>
        <li>Reversing things</li>
        <li>Keeping track of state</li>
        <li>Add/remove from back of a structure</li>
    </ul>
    <br>
    Stacks are best to help keep state
    <br>
    Stacks are advantageous for last in, first out
    <br>
    Queue are advantageous for first in, first out (FLFO)
</details>
<details>
    <summary><strong>Quiz</strong></summary>
    <strong>How do queues differ from stacks?</strong>
    <br>
    Queues use FIFO and stacks use LIFO.
    <br>
    <br>
    <strong>What is wrong with the following Java code?</strong>

```
import java.util.Stack;
public class MyClass {
      public static void main(String args[]) {
          Stack myStack = new Stack();
          myStack.push("test");
          myStack.pop();
          myStack.pop();
```
It attempts to pop from an empty stack.
    <br>
    <br>
    <strong>The following Swift code uses the push and pop functions as in the example. What is the value of SecondPop?</strong>
    <br>

```
var deck:Stack=Stack()
deck.push(item: "Queen: Spades")
deck.push(item "10: Diamonds")
deck.push(item: "4: Hearts")
deck.push(item: "2: Hearts")
var FirstPop = deck.pop()
var SecondPop= deck.pop()
```
4: Hearts
    <br>
    <br>
    <strong>In the Swift code func pop()-> String?, what does the question mark mean?</strong>
    <br>
    The value returned is either a string or nil.
    <br>
    <br>
    <strong>Which data structure is most useful for reversing an ordered state or list?</strong>
    <br>
    a stack
    <br>
    <br>
    <strong>What does LIFO stand for?</strong>
    <br>
    last in first out
    <br>
    <br>
    <strong>How are items with the same priority dequeued from priority queues?</strong>
    <br>
    by FIFO
    <br>
    <br>
    <strong>The following Swift code uses the Queue class as in the example. What does the print() function output?</strong>
    <br>

```
var yourQueue = Queue()
yourQueue.enqueue(item: "10")
yourQueue.enqueue(item: "5")
yourQueue.enqueue(item: "8")
var OutZero yourQueue.dequeue()
var OutOne = yourQueue.dequeue()
print(yourQueue.peek()!)
```
8
    <br>
    <br>
    <strong>What does a peek() return from a queue?</strong>
    <br>
    the first item
</details>

### Hash-Based Data Structures

<details>
    <summary><strong>What are associative arrays?</strong></summary>
    <strong>Associative Array:</strong> Collection of key-value parirs
    <br>
    Example: Sacramento: California
    <br>
    <br>
    <strong>Associated Array Rules</strong>
    <br>
    <ul>
        <li>Key-Value paris are bound together</li>
        <li>Each key must be unique</li>
        <li>Order isn't important</li>
        <li>Values are accessed with the key</li>
        <li>Values do not need to be unique</li>
    </ul>
</details>
<details>
    <summary><strong>Understanding Hash Functions</strong></summary>
    <strong>Hashing:</strong> is a way of taking some raw data and mixing it together to form a smaller single piece of data
    <br>
    <strong>Hash Inputs</strong>
    <br>
    <ul>
        <li>Characters</li>
        <li>Objects</li>
        <li>Numbers</li>
    </ul>
    <br>
    <strong>what's so great about hash function? </strong>
    <br>
    hash function are not reversible they are one way.
    <br>
    This means you cannot feed the hash value into another function and get the original data back
    <br>
    <br>
    <strong>Benefite of Hashing</strong>
    <br>
    Example: let's say a bank has database of a bunch of usernames and passwords. then a hacker comes along and somehow gains access to the database and has access to this information. Obviously this would be very bad if the passwords were stored in plain text because now the hacker would have direct access to everyone's login information.
    <br>
    However, as a security measure you could store a hash of the passwords instead. then when someone logs in, you could put their password, the series of characters, through the hash function and see if the resulting hash value matches the hash value you have stored in the database
    <br>
    <br>
    <strong>ASCII:</strong> Numerical representation of text characters
    <br>
    Example: T = 116,  W = 119
    <br>
    <br>
    <strong>Collision:</strong> Anytime two inputs produce the same hash value - when two keys have the same hash value
    <br>
    <br>
    <strong>How Hashing Works</strong>
    <br>
    <ul>
        <li>Password: twentytwoever</li>
        <li>ASCII Value: 1463   </li>
    </ul>
</details>
<details>
    <summary><strong>Understanding hash tables</strong></summary>
    <strong>A Hash Table</strong> is an implementaiton of the <strong>associative array abstract data structure</strong>
    <br>
    <br>
    <strong>Adding Key-Value Paris</strong>
    <br>
    <ul>
        <li>Always added as a set</li>
        <li>
            Keywords vary be language
            <ul>
                <li>Put</li>
                <li>Add</li>
                <li>Insert</li>
            </ul>
        </li>
    </ul>
    <br>
</details>
<details>
    <summary><strong>Using dictionaries in python</strong></summary>

```
statusToCapitals = {}

statusToCapitals["Texas"] = "Austing"
statusToCapitals["New York"] = "Albany"

print(statusToCapitals["New York"])
```
</details>
<details>
    <summary><strong>Language support for hashing</strong></summary>
    <strong>Hashing in Various Languages</strong>
    <br>
    <table>
        <tr>
            <td>Java</td>
            <td>hashCode function</td>
        </tr>
        <tr>
            <td>Swift</td>
            <td>hashValue property</td>
        </tr>
        <tr>
            <td>.Net</td>
            <td>GetHashCode function</td>
        </tr>
        <tr>
            <td>Python</td>
            <td>GetHashCode function</td>
        </tr>
        <tr>
            <td>Ruby</td>
            <td>GetHashCode function</td>
        </tr>
        <tr>
            <td>Javascript with Node.js</td>
            <td>npm install an appropraite module</td>
        </tr>
    </table>
    <br>
    A hash value is based on what it means for two objects to be equal
</details>
<details>
    <summary><strong>Language support for hash tables</strong></summary>
    <strong>Hash Tables across Languages</strong>
    <br>
    <ul>
        <li>Python: dict type</li>
        <li>Swift: dictionaries</li>
        <li>Ruby: hash class</li>
        <li>Javascript: Objects as associative arrays</li>
        <li>C#/.NET: hash table in System.Collections</li>
        <li>Java: hash table and hash map collecitons</li>
    </ul>
</details>
<details>
    <summary><strong>Pros and Cons of hash-based structures</strong></summary>
    Hash map operations always take the same amount of time, regardless of the size of the hash table
    <br>
    <strong>Hash Map Operations</strong>
    <br>
    <ul>
        <li>Search: O(1)</li>
        <li>Insertion: O(1)</li>
        <li>Deletion: O(1)</li>
    </ul>
    <br>
    Hash tables are excellect at managing many key-value pairs and volatile data
</details>
<details>
    <summary><strong>Quiz</strong></summary>
    <strong>Which language has the least support for hash functions and tables?</strong>
    <br>
    JavaScript
    <br>
    <br>
    <strong>Which line in the following Python 3 code produces a Key Error?</strong>
    <br>

```
# Key: Capital
# Value: State
CapitalsToStates = {}
CapitalsToStates["Austin"] = "Texas"
CapitalsToStates["Albany"] = "New York"
print(CapitalsToStates["New York"])
print(CapitalsToStates["Austin"])
```
print(CapitalsToStates["New York"])
    <br>
    <br>
    <strong>Why would you use separate chaining?</strong>
    <br>
    to resolve a collision
    <br>
    <br>
    <strong>When do hash tables suffer in performance?</strong>
    <br>
    when there are collisions
    <br>
    <br>
    <strong>How does hashing differ from encrypting?</strong>
    <br>
    Encrypting is reversible, but hashing is not.
    <br>
    <br>
    <strong>Which statement is true for associative arrays?</strong>
    <br>
    Keys must be unique.
</details>

### Trees and Graphs

<details>
    <summary><strong>What are sets?</strong></summary>
    <strong>Set</strong>
    <ul>
        <li>A collection of unique items</li>
        <li>Order doesn't matter</li>
        <li>None of the elements are duplicated</li>
    </ul>
    <br>
    1. Take an object
    <br>
    2. Hash the object
    <br>
    3. Store the object using the index
    <br>
    <strong>Membership</strong>
    <br>
    typesOfClothing = {pants, shirts, skirts, shorts}
    <br>
    <br>
    <strong>Implementation</strong>
    <br>
    <ul>
        <li>Array (linear search)</li>
        <li>Linked list (travers)</li>
    </ul>
</details>
<details>
    <summary><strong>Sets in Python?</strong></summary>

```
primaryColors = frozenset(["red", "blue", "yellow"])

color = "green"

if color.lower() in primaryColors:
    print(color + " is a primary color")
else:
    print(color + " is not a primary color")

letters = set(['a', 'b'])
letters.add('c')
print(letters)
```
</details>
<details>
    <summary><strong>Introduction to tree data structures</strong></summary>
    Child nodes with the same parent are siblings
    <br>
    A node with no children is a leaf
    <br>
    <br>
    <strong>What Each Node Can have</strong>
    <br>
    <ul>
        <li>Many children</li>
        <li>Just one child</li>
        <li>No children</li>
    </ul>
    <br>
    <br>
    <img src="https://lh5.googleusercontent.com/zQ8iFEPd3u2oX__Sm3Gl4pcJTrrnCsUr6Ji8arQ70eu6oO1tnTlIdIZaYSR4x7T9YChDEhECTBsTSntW8FFc=w1366-h625-rw">
</details>
<details>
    <summary><strong>Understanding binary search trees</strong></summary>
    Binary search trees are used to implement another data structure
    <br>
    <ul>
        <li>C++: sets are implemented with BSTs</li>
        <li>C#, .NET: sorted dictionaires are implemented with BSTs</li>
        <li>Java: TreeMap implemented with a red-black tree</li>
        <li>Javascript, Ruby, Python: Third-party implementations available</li>
    </ul>
</details>
<details>
    <summary><strong>Understand Heaps</strong></summary>
    <strong>Heap:</strong> A data structure implemented as a binary tree
    <br>
    binary tree is where each parent had a maximum of two direct child nodes
    <br>
    <strong>What makes a heap special?</strong>
    <br>
    heaps are collection of objects, as we add items to the heap, they are always top to bottom, left to right
    <br>
    <strong>Priority Queue</strong>
    <br>
    <ul>
        <li>Order doesn't matter</li>
        <li>Heaps are used to implement</li>
    </ul>
</details>
<details>
    <summary><strong>Pros and Cons of tree data structures</strong></summary>
    Binary Search Tree: maintain sorted order while staying fast for insertion, deletion, and accessing
    <br>
    Heaps: great for priority queues
    <ul>
        <li>Find min/max: 0(1)</li>
        <li>Insert: 0(log(N))</li>
        <li>Search: 0(N)</li>
        <li>Delete: 0(N)</li>
    </ul>
</details>
<details>
    <summary><strong>Quiz</strong></summary>
    <strong>Which statement is true for a tree data structure?</strong>
    <br>
    The root does not have a parent.
    <br>
    <br>
    <strong>What does the following Python 3 code output?</strong>
    <br>

```
pocketContents=set(["keys","coins","knife"])
pocketContents.add("receipt")
pocketContents.add("string")
print(pocketContents)
```
{'receipt', 'coins', 'keys', 'string', 'knife'}
    <br>
    <br>
    <strong>Which list constitutes a valid set containing four elements?</strong>
    <br>
    {0, "dog", "car", 7}
    <br>
    <br>
    <strong>What characterizes a min heap?</strong>
    <br>
    The root contains the lowest value.
    <br>
    <br>
    <strong>Why are binary search trees organized with the left child less than the parent and the right child greater than the parent?</strong>
    <br>
    to make them easy to search
</details>
