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
            <td> 16 bits </td>
        </tr>
        <tr>
            <td> Int </td>
            <td> ~-3 billion to ~2 billion </td>
            <td> 32 bits </td>
        </tr>
            <tr>
            <td> Long </td>
            <td> -(2^63)  to (2^63) </td>
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
    <br>
    <br>
    <strong>signed and unsigned data</strong>
    <br>
    <ul>
        <li><strong>signed data type</strong>can store the positive and negative numbers </li>
        <li><strong>unsigned data type</strong>can store only the positive</li>
    </ul>
    <br>
    byte is 8 bit => each byte can represent a letter
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
    <strong>Data Structures:</strong>is a collection with defined way of accessing and sorting items is referenced data types.
    <br>
    are containers they allow us to combine several pieces of data into a single structure
    <br>
    - have a specialized way and format of organizing and storing these pieces.
    - Data structures give us organization, storage, and access.
    <br>
    <br>
    <strong>Why use a data structure?</strong>
    <br>
    we could have created individual variables for every student and store the appropriate number of pets each student has in each variable
    <br>
    <strong>what exact size of data structure</strong>
    <br>
    depends allocated space for structure Number of piece of data size of each data piece
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
    <strong>String</strong>
    <ul>
        <li>Is a Referenced data type</li>
        <li>Is a data type composed of a sequence of characters.</li>
        <li>It's a data type that's built out of another data type.</li>
        <li>Its implemented with a data structure</li>
    </ul>
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
<br>
    every element in the array have an unique index the index start from 0
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
    <br>
     2d array is an array and every element in the array is an array itself The rule is that every inner array must have the same number of elements
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
    <br>
    like multidimensional array but each inner array can have different number of elements
    <br>
    this means that if we're iterating through the array we'll need to access the length of each individual array because their sizes can be different.
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
        <li>Pass your data structure as a parameter to a sorting function</li>
    </ul>
    <br>
    when sorting objects you must define which attribute the objects will be sorted accordingly  this called Defining a comparator to sort
</details>
<details>
    <summary><strong>Big O notation</strong></summary>
    <strong>Big O Notation</strong> Notation used to describe the performance or complexity of an algorithm
    <br>
    classifies performance as the input size grows
    <br>
    "O" indicate the order of operation: time scale to perform an operation
    <br>
    It usually describes the worst case scenario of how long it takes to perform a given operation.
    <br>
    Many algorithms and data structures have more than one O inserting data, searching for data, deleting data, etc.
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

### Lists
<details>
    <summary><strong>Operations on linked lists</strong></summary>
    <ul>
        <li>
          <strong>Add</strong>
          <br>
           To add an item, it's easiest to insert at the back or front of the list.
          <br>
           When inserting at the front, we can initialize the new node with the appropriate data and set the new node's next pointer to point to the first node.
          <br>
           When inserting at the back of the list, we take the last node of the list and set its next pointer to our new node.
          <br>
        </li>
        <li>
            <strong>Access</strong>
            <br>
            To access an item, we don't have to have an index like we do with an array.
            <br>
            This means we have to follow the pointers until we find the item we want to access.
        </li>
        <li>
            <strong>Delete</strong>
            <br>
            To delete an item, we first have to find the item and then, update the next pointer of the node preceding and following that node.
        </li>
        <li>
            <strong>Search</strong>
            <br>
            to search for an item We have to traverse through the entire list to find anode with a specific value or find out that the data does not even exist in the list.
        </li>
        <li>
            <strong>Insert</strong>
            <br>
            Let's say we wanted to add a train car somewhere else in the list.
            <br>
            We'd have to follow the pointers to that specific place and then update the pointers so that the previous train car points to our new train car and our new train car points to the next element.
        </li>
    </ul>
    <br>
    <strong>linked list:</strong>the elements of a linked list are not stored at contiguous locations. Instead, we link the elements using pointers.
    <br>
    is a linear collection of data elements called nodes contain reference to the next node in the list Hold whatever data the application needs
    <br>
    <br>
    <strong>node:</strong>contains data and a pointer to the next node the first item you add to the list called the head
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
    <strong>each item has point to the next item in the list</strong>
    <br>
    <br>
    <strong>doubly Linked</strong> we have a next and previous pointer and we can go through the list forward or backward
    <br>
    <strong>each item in the list has two pointers to the next and previous element </strong>
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
    <summary><strong>Pros and Cons of lists</strong></summary>
    <strong>inserting and deleting</strong>
    <br>
    elements can be easily [inserted] and [removed] with O(1) performance
    <br>
    This is because linked lists have next pointers and do not need to be stored contiguously in memory
    <br>
    underlying memory doesn't need to be reorganized
    <br>
    <br>
    <strong>Cons:</strong>
    <br>
    <ul>
        <li>
            <strong>Access</strong>
            Can't do constant-time random item access
            <br>
            Item lookup[Access] is linear in time complexity (O(n))
            <br>
            because items don't have index or even keywords
        </li>
        <li>
            <strong>Updating</strong>
            take O(n) time
            <br>
            because we need to find the appropriate node and then update its value.
        </li>
        <li>
            <strong>Searching and deleting</strong>
            take linear, or O of N time in the worst case,
            <br>
            because we have to search for the element in order to find it, access it, and delete it
        </li>
    </ul>
    <br>
    Sorting: Merge sort is often preferred for sorting a linked list.
    <br>
    Other algorithms, such as quick sort and heap sort are not ideal because linked lists have slow, random access performance.
    <br>
    <br>
    In random access, we should be able to say an index and get the item at that slot immediately, like in array.
</details>

### Stacks and Queues
<details>
    <summary><strong>What are stacks</strong></summary>
    <strong>Stacks</strong> is an ordered series of objects just like a list but its intended use is slightly different we push objectives on to the stack and pop objects off of it
    <br>
    collection that support push and pop operations
    <br>
    stacks are great for programs where you need to reverse things
    <br>
    Stacks are also good for keeping track of state as things are pushed on and popped off the stacks
    <br>
    <strong>(LIFO)</strong> Last in, First out -> The last item pushed is the first one popped
    <br>
    <br>
    if you wanted to add or remove from the bottom of the stack, you would have to lift the entire stack in order to add that item.
    <br>
    This is why for stacks we add and remove from the top.
    <br>
    <br>
    <strong>stacks Uses</strong>
    <br>
    <ul>
        <li>Expression processing </li>
        <li>Backtracking: browser back stack, for example Error tracing </li>
    </ul>
    <br>
    <strong> Stacks are great for </strong>
    <br>
    <ul>
        <li>Reversing things </li>
        <li>Keeping track ot state </li>
        <li>Add/remove from the back of structure </li>
    </ul>
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
    collection that supports adding and removing - follow FIFO  rule - first in first out - first item added is the first item out
    <br>
    <br>
    <strong>Enqueue</strong> is when an item is added to a list
    <br>
    <strong>Dequeue</strong> is when an item is removed from the list
    <br>
    <strong>Peek</strong>See the first item in the queue without removing it
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
    <strong>Priority Queue</strong>
    <br>
    <ul>
        <li>Each element has a priority associated with it</li>
        <li>if you add multiple items that have the same priority, they will queue as normal first-in, first-out order Not supported in all languages </li>
    </ul>
    <br>
    Java has priority queues
    <br>
    C++ has a priority container
    <br>
    <br>
    <storng>D-E-Q-U-E-K -> Double-ended queue</storng>
    <ul>
        <li>double-ended queue is like having a stack and a queue at the same time.</li>
        <li>have a collection of items and we can add new items to this, but we can choose to add and remove from either end.</li>
        <li>restriction is we can't remove from anywhere else in the collection. </li>
    </ul>
    <br>
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
    <br>
    for small datasets, arrays are usually more efficient hash tables don't order entries in predictable way
    <br>
    <strong>Advantages:</strong>
    <br>
    <ul>
        <li>every item have a key. </li>
        <li>a key that allows us to access our data in a meaningful way.</li>
        <li>Key-value pair are bound together.</li>
        <li>key-to-value mapping are unique.</li>
        <li>value do not accessed with the key.</li>
        <li>Keys are mapped to data values by using a hash to compute an index value.</li>
        <li>hash tables are typically are usually more efficient.</li>
        <li>Order Isn't important.</li>
    </ul>
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

