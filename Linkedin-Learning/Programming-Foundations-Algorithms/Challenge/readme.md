### Challenge

<details>
    <summary><strong>Overview Quiz</strong></summary>
    <strong>An algorithm that takes eight times longer to operate on a data set that is twice as large is said to be _____ in time.</strong>
    <br>
    cubic
    <br>
    <br>
    <strong>An algorithm that is deterministic _____.</strong>
    <br>
    always produces the same outputs from a given set of inputs
    <br>
    <br>
    <strong>Which classifications apply to Euclid's algorithm for finding the least common denominator?</strong>
    <br>
    exact and deterministic
    <br>
    <br>
    <strong>Which algorithm type derives a new set of data from an existing set of data?</strong>
    <br>
    a computational algorithm
    <br>
    A computational algorithm uses calculations to derive and output new data from another set of input data.
    <br>
    <br>
    <strong>The measurement of algorithm performance is dependent on which criteria?</strong>
    <br>
    the input data
    <br>
    The measurement of performance for an algorithm is dependent on the input data and varies as the input size grows.
    <br>
    <br>
    <strong>What is the purpose of an algorithm?</strong>
    <br>
    to solve a specific problem with a sequential set of steps
    <br>
    An algorithm is used to solve a specific problem by following a sequential set of steps.
</details>

<details>
    <summary><strong>Comman Data Strucutres Quiz</strong></summary>
    <strong>What benefit does a linked list provide?</strong>
    <br>
    underlying memory does not need to be contiguous
    <br>
    The underlying memory that holds any node data does not need to be contiguous for a linked list.
    <br>
    <br>
    <strong>What criteria allows algorithms to execute efficiently?</strong>
    <br>
    the scenario and available data structure types
    <br>
    <br>
    <strong>In the example linear array, how are the elements referenced using index values? </strong>
    <br>
    0,1,2,3,4
    <br>
    Elements in an array are referenced by index values, typically starting at 0.
    <br>
    <br>
    <strong>Why are hash tables favored over arrays or linked lists?</strong>
    <br>
    They are faster for item lookups.
    <br>
    <br>
    <strong>Why are linked lists sometimes preferred over arrays?</strong>
    <br>
    Why are linked lists sometimes preferred over arrays?
    <br>
    <br>
    <strong>According to the code snippet below, which element will be removed from the queue?</strong>
    <br>
    1
    <br>
    A queue uses a first-in, first-out approach. Since element 1 is added first, it is the first to be removed with the pop instruction.
    <br>
    <br>
    <strong>Stacks are _____ data structures.</strong>
    <br>
    last in, first out
    <br>
    <br>
    <strong>How does a hash table map index values to data values?</strong>
    <br>
    Keys are mapped to data values by using a hash to compute an index value.
    <br>
    A hash table is an associative array where a hash function uses a key to compute an index value and to map to the data value.
    <br>
    <br>
    <strong>Which data structure is most analogous to a dictionary?</strong>
    <br>
    a hash table
    <br>
    <br>
    <strong>What does the below code do, when working with a linked list?</strong>
    <br>

```
1 new_node = Node(data)
2 new_node.set_next(self.head)
3 self.head = new_node
4 self.count += 1
```
It add a new node and makes it the head of the list.
<br>
When a new value (node) is inserted in a linked list, the head can point to the new node by using the self.head = new_node code.
    <br>
    <br>
    <strong>Which data structure operation would be used for an “undo” command?</strong>
    <br>
    a stack using last-in, first-out
    <br>
    A stack is useful in providing backtracking features such as an undo button. An undo button would process the last command used as the first to undo.
    <br>
    <br>
    <strong>How many elements are in an 8 by 3 by 2 array?</strong>
    <br>
    48
</details>

<details>
    <summary><strong>Recursion Quiz</strong></summary>
    <strong>Which is the defining property of a recursive function?</strong>
    <br>
    It calls itself.
    <br>
    <br>
    <strong>What would the following code return for efun(8)?</strong>
    <br>

```
def efun(num):
  if num==0:
  return 1
  else:
  return num * efun(num-2)
```
384
    <br>
    <br>
    <strong>In the following recursion, what is the breaking condition?</strong>
    <br>
```
function countup(x) {
  if (x == 128)
  return
 else
  countup(x+1)
 }
```
if (x == 128)
    <br>
    <br>
    <strong>How is recursion implemented in functions?</strong>
    <br>
    A function calls itself from within its own code.
    <br>
    With recursion, a function calls itself from within its own code. This is useful for creating a loop where the same logic is required with each execution.
    <br>
    <br>
    <strong>What happens when executing a return statement in a recursive function?</strong>
    <br>
    The program returns to the statement after the function call was made.
    <br>
    The program returns to the statement after the function call was made. If there is no statement, the program exits the function.
</details>

<details>
    <summary><strong>Sorting Data Quiz</strong></summary>
    <strong>Which of the following sorted datasets would be easiest for a user to understand?</strong>
    <br>
    a list of items that are ordered by price from lowest to highest
    <br>
    Sorting data benefits a user by ordering it in a way that makes it easily understandable for users. A list from high to low is an example of a sorted list.
    <br>
    <br>
    <strong>How does a bubble sort find the largest value in a data set?</strong>
    <br>
    All value pairs are compared to each other until the largest is at the top.
    <br>
    With a bubble sort, two values are compared to each other incrementally, the largest value is shifted until it is at the top.
    <br>
    <br>
    <strong>Which condition is true after the end of one recursion step in a quicksort?</strong>
    <br>
    The pivot element is placed at its correct array location.
    <br>
    <br>
    <strong>What method does a merge sort use to break down data and sort it?</strong>
    <br>
    It uses recursion to break down data into smaller sets in order to find the appropriate order.
    <br>
    A merge sort uses recursion. It breaks down the data into smaller manageable sets. As it sorts the smaller sets, it gradually rebuilds and works its way up to the original full data set.
    <br>
    <br>
    <strong>What are present in bubble-sort codes that indicate their time complexity?</strong>
    <br>
    nested loops
    <br>
    <br>
    <strong>A programmer needs to organize a data set. How will a quick sort accomplish this?</strong>
    <br>
    It will use a pivot point and move items that are on the wrong side of the pivot value by using high and low index values.
    <br>
    A quick sort sets a pit point to partition a data set. High and low index values are then used to rearrange data values that are on the "wrong" side of the pivot point.
    <br>
    <br>
    <strong>How does the required time for a merge sort grow with the size of the data set?</strong>
    <br>
    logarithmic-linear
</details>

<details>
    <summary><strong>Searching Data Quiz</strong></summary>
    <strong>Given that it is faster to search ordered lists, what is the downside of using them?</strong>
    <br>
    They are more time consuming to create and maintain than unordered lists.
    <br>
    <br>
    <strong>Why does a test for ordering require an algorithm that is linear in time complexity?</strong>
    <br>
    It must test every element.
    <br>
    <br>
    <strong>A developer routinely uses code to search an unordered list. As more items are added to the list over time, what does the developer notice about efficiency with the search?</strong>
    <br>
    The search time is increased relative to the number of items added to the list.
    <br>
    As the unordered list search is based on linear time complexity, the number of the items that are added to the list increases the overall search time. This is very noticeable when the value being searched is near the end of the list or it doesn't exist at all.
    <br>
    <br>
    <strong>A developer decides to sort data rather than search for data. If the developer wants to find a specific number, how does the sort find the desired value</strong>
    <br>
    Indexes are created at the beginning and end of the list and a midpoint is calculated. Values are searched between the index and midpoint. The indexes move based on the results.
    <br>
    Searching an ordered list is efficient. Low and high index values and a midpoint is created in the data set. If the value is not found between an index value and the midpoint, new index values are established. This repeats until the value is found.
    <br>
    <br>
    <strong>Searching in an unordered list requires computational time that is _____ in the list size.</strong>
    <br>
    linear
</details>

<details>
    <summary><strong>Other Algorithms</strong></summary>
    <strong>What does the line counter[item] = 1 do in the code below?</strong>
    <br>

```
for item in items:
  if (item in counter.keys():
  counter[item] +=1
  else:
  counter[item]=1
```
It creates a dictionary entry for item and sets its value to one.
    <br>
    <br>
    <strong>Finding the maximum value recursively has the same time complexity as _____</strong>
    <br>
    an unordered list search
    <br>
    <br>
    <strong>Which result happens when you add a redundant entry to a hash table?</strong>
    <br>
    The new entry replaces the old one.
    <br>
    <br>
    <strong>Which line in the code snippet below adds content to a hash table?</strong>
    <br>

```
1 items = ["apple", "pear", "orange", "banana", "apple","orange", "apple", "pear", "banana", "orange","apple", "kiwi", "pear", "apple", "orange"]

2 filter = dict()

3 for key in items:
4       filter[key] = 0

5 result = set(filter.keys())
6       print(result)
```
3
<br>
The code in line 3 performs a loop over each defined item and then adds it to the hash table.
    <br>
    <br>
    <strong>Evaluate the code snippet below. At what point does recursion occur when using an algorithm to find the highest value in a data set?</strong>
    <br>

```
1 def find_max(items):
2     if len(items) == 1:
3         return items[0]
4 op1 = items[0]
5 print(op1)
6 op2 = find_max(items[1:])
7 print(op1, op2)
```
line 6
<br>
Recursion occurs when a function calls itself. With this code snippet, a function find_max is defined and that function is called within itself at line 6. This repeats the process of the function.
</details>

