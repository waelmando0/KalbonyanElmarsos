### Challange

<details>
    <summary><strong>Quiz 1</strong></summary>
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
<details>
    <summary><strong>Quiz 2</strong></summary>
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
<details>
    <summary><strong>Quiz 3</strong></summary>
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
<details>
    <summary><strong>Quiz 4</strong></summary>
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
<details>
    <summary><strong>Quiz 5</strong></summary>
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
<details>
    <summary><strong>Quiz 6</strong></summary>
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
