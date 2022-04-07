## Programming Foundations: Algorithms

### Introduction
<details>
    <summary><strong>What you should know</strong></summary>
    <ul>
        <li>Basic principle of programming</li>
        <li>using a text editor to write and debug code</li>
        <li>Knowledge of a language like Python, java and C#</li>
    </ul>
</details>

### Overview
<details>
    <summary><strong>What are algorithms?</strong></summary>
    <strong>Algorithm Characteristics</strong>
    <br>
    <ul>
        <li>
            Algorithm Complexity
            <ul>
                <li>Space Complexity: How much memeory does it require?</li>
                <li>Time Complexity: How much time does it take to complete?</li>
            </ul>
        </li>
        <li>
            Inputs and output
            <ul>
                <li>What does the algorithm accept, and what are the results?</li>
            </ul>
        </li>
        <li>
            Classificaiton
            <ul>
                <li>Serial/Parallel, exact/approximate</li>
                <li>deterministic/non-deterministic</li>
            </ul>
        </li>
    </ul>
</details>
<details>
    <summary><strong>Common algorithms in programming</strong></summary>
    <strong>Common Algorithms</strong>
    <br>
    <ul>
        <li>
            Search algorithms
            <ul>
                <li>Find specific data in a structure (for example, a substring within a string)</li>
            </ul>
        </li>
        <li>
            Sorting algorithms
            <ul>
                <li>Take a dataset and apply a sort order to it</li>
            </ul>
        </li>
        <li>
            Computational algorithms
            <ul>
                <li>Given one set of data, calcuate another (is a given number prime?)</li>
            </ul>
        </li>
        <li>
            Collection algorithms
            <ul>
                <li>Work with colletions of data (count specific items, nevigate among data elements, filter out unwanted data, etc</li>
            </ul>
        </li>
    </ul>
    <br>
    <br>
    <strong>Example: Euclid's Algorithm</strong>
    <br>
    Find the greatest common denominatore (GCD) of two integats:
    <br>
    Example: GCD of 20 and 8 is 4
    <br>
    (because 8 / 4 is 2; and 20 / 4 is 5)
    <br>
    <br>
    1. For two integers a and b where a > b divide a by b
    <br>
    2. If the remainder, r is 0 then stop: GCD is b
    <br>
    3. Otherwise set a to b, b to r and repeat at step 1 untile r is 0
    <br>
    <table>
        <tr>
            <td><strong>GCD (20, 8)</strong></td>
        </tr>
        <tr>
            <td>a</td>
            <td>b</td>
            <td>r</td>
        </tr>
        <tr>
            <td>20</td>
            <td>8</td>
            <td>4</td>
        </tr>
        <tr>
            <td>8</td>
            <td>4</td>
            <td>0</td>
        </tr>
    </table>
    <br>

```
def gcd(a, b):
    while (b != 0):
        t = a
        a = b
        b = t % b

    return a

print(gcd(60, 96))
print(gcd(20, 8))
```
</details>
<details>
    <summary><strong>Measuring algorithm performance</strong></summary>
    <strong>Understanding Algorithm Performance</strong>
    <br>
    <ul>
        <li>Measure how an algorithm responds to dataset size</li>
        <li>
            Big-o notation
            <ul>
                <li>Classifies performance as the input size grows</li>
                <li>"O" indicates the order of operation: time scale to perform an operation</li>
            </ul>
        </li>
        <li>Many algorithms and data structures have more than one O</li>
    </ul>
    <br>
    <br>
    <strong>Common Big-O Terms</strong>
    <br>
    <table>
        <tr>
            <td>Notation</td>
            <td>Description</td>
            <td>Example</td>
        </tr>
        <tr>
            <td>O (1)</td>
            <td>Constant time</td>
            <td>Looking up a single element in an array</td>
        </tr>
        <tr>
            <td>O (log n)</td>
            <td>Logarithmic</td>
            <td>Finding an item in a sorted array with a binary search</td>
        </tr>
        <tr>
            <td>O (n)</td>
            <td>Linear time</td>
            <td>Searching an unsorted array for a specific value</td>
        </tr>
        <tr>
            <td>O (n log n)</td>
            <td>Log-linear</td>
            <td>Complex sorting algorithms like heap sort and merge sort</td>
        </tr>
        <tr>
            <td>O (n2)</td>
            <td>Quadratic</td>
            <td>Simple sorting algorithms, such as bubble sort, selection sort, and insertion sort</td>
        </tr>
    </table>
</details>

### Comman Data Structure

<details>
    <summary><strong>Introduction to data structures</strong></summary>
    <strong>Overview of Data Strucutres</strong>
    <br>
    used to organize data so it can be processed
    <br>
    <strong>Common Data Structures</strong>
    <br>
    <ul>
        <li>Arrays</li>
        <li>Linked lists</li>
        <li>Stacks and queues</li>
        <li>Trees</li>
        <li>Hash tables</li>
    </ul>
</details>

<details>
    <summary><strong>Arrays</strong></summary>
    <strong>Data Strucutes: Arrays</strong>
    <br>
    <ul>
        <li>Collection of elements identified by index or key</li>
        Arrays in most languages start their indexes at zero for the first element
    </ul>
    <br>
    <strong>Array Operation</strong>
    <br>
    <ul>
        <li>Calculate item index: O(1)</li>
        <li>Inseart or delete item at beginning: O(n)</li>
        <li>Inseart or delete item at middle: O(n)</li>
    </ul>
</details>

<details>
    <summary><strong>Linked Lists</strong></summary>
    <strong>Linked Lists</strong>
    <br>
    <ul>
        <li>Collections of data elements, called nodes</li>
        <li>Contain reference to the next node in the list</li>
        <li>Hold whatever data the application needs</li>
        <li>Elements can be easily inserted and removed</li>
        <li>Underlying memory doesn't need to be reorganized</li>
        <li>Can't do constant-time random item access</li>
        <li>Item loopup is linear in time complexity (O(n))</li>
    </ul>
    <br>
</details>

<details>
    <summary><strong>Stacks and queues</strong></summary>
    <strong>Stacks</strong>
    <br>
    <ul>
        <li>Stack: Collection that supports push and pop operation</li>
        <li>The Last item pushed is the first one popped</li>
    </ul>
    <br>
    <strong>Queues</strong>
    <br>
    <ul>
        <li>Queue: Collection that supports adding and removing</li>
        <li>First item added is the first item out</li>
    </ul>
    <br>
    <br>
    <strong>Practical Applications</strong>
    <br>
    <ul>
        <li><strong>Stack</strong>
            <ul>
                <li>Expression Processing</li>
                <li>Backtracking: browser back stack</li>
            </ul>
        </li>
        <li><strong>Queue</strong>
            <ul>
                <li>Order processing</li>
                <li>Messaging</li>
            </ul>
        </li>
    </ul>
</details>

<details>
    <summary><strong>Stacks and Queues Walkthrough</strong></summary>


```
# create a new empty stack
stack = []

# Push items onto the stack
stack.append(1)
stack.append(2)
stack.append(3)
stack.append(4)

# Print the stack contents
print(stack)

# pop an item off the stack
x = stack.pop()
print(x)
print(stack)
```



```
# try out the python queue functions
from collections import deque

# create a new empty deque object that will functions as a queue
queue = deque()

# add some items onto the queue
queue.append(1)
queue.append(2)
queue.append(3)
queue.append(4)

# Print the queue contents
print(queue)

# pop an item off the front of the queue
x = queue.popleft()
print(x)
print(queue)
```
</details>

<details>
    <summary><strong>Hash Tables</strong></summary>
    <strong>Hash tables</strong>
    <br>
    it's a data structure that maps keys to their associated values, and it does this using what's calle a hash function, this function uses the key to compute an index into the slots that are in the hash table and map the key to the value
    <br>
    <strong>Hash Tables</strong>
    <br>
    <ul>
        <li>Key-to-value mappings are unique</li>
        <li>Hash tables are typically very fast</li>
        <li>For small datasets, arrays are usally more efficient</li>
        <li>Hash tables don't order entries in a predictable way</li>
    </ul>
    <br>

```
# create a hashtable all at once
items1 = dict({"key": 1, "key2" : 2, "key3" : "three"})
print(items1)

# create a hashtable progressively
items2 = {}
items2["key1] = 1
items2["key2] = 2
items2["key3] = 3
print(items2)

# try to access a nonexistent key
# print(items1["key6"])

# replace an item
items2["key2"] = "two"
print(items2)

# iterate the keys and values in the dictionary
for key, value in items2.item():
    print("key: ", key, " Value: ", value)


</details>