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
    <strong>Algorithm: </strong>a set of instructions that describes how to get the exact result you want
    <br>
    The purpose of an algorithm is to solve a specific problem with a sequential set of steps
    <br>
    <br>
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
                <li>
                    <strong>Serial/Parallel</strong>
                    some algorithms work on their data sets in sequential fashion, which means that they are serial in nature.
                    <br>
                    Whereas a parallel algorithm can break up a data set into smaller pieces and then work on each simultaneously.
                </li>
                <li>
                    <strong>exact/approximate</strong>
                    An algorithm can be exact, in which case it produces a known predictable value.
                    <br>
                    or it can be approximate, in which case, it tries to find an answer that might or might not be exact.
                    <br>
                    For example, a facial recognition algorithm might not give the same answer every single time.
                </li>
                <li>
                    <strong>deterministic/non-deterministic</strong>
                    algorithms can be deterministic, in which case it executes each step with an exact decision.
                    <br>
                    or it could be non-deterministic, in which it attempts to produce a solution using successive guesses.
                    <br>
                    which become more accurate over time.
                </li>
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
    1. If the remainder, r is 0 then stop: GCD is b
    <br>
    1. Otherwise set a to b, b to r and repeat at step 1 untile r is 0
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
<br>

```
let's try to figure out how this algorithm worked in the followed example:
print(gcd(60, 96))
--state =>   a = 60 ,  b = 96
  1- assign t to a   meaning t = 60
  2- assign a to b   meaning a = 96
  3- assign b to the reminder of divide t by b
  meaning  b = 60 % 96  =>  60
--state a = 96 , b = 60
  1- assign t to a   meaning t = 96
  2- assign a to b   meaning a = 60
  3- assign b to the reminder of divide t by b
  meaning  b = 96 % 60  =>  36
--state =>  a = 60 , b = 36
  1- assign t to a   meaning t = 60
  2- assign a to b   meaning a = 36
  3- assign b to the reminder of divide t by b
  meaning  b = 60 % 36  =>  24
--state => a= 36 , b = 24
  1- assign t to a   meaning t = 36
  2- assign a to b   meaning a = 24
  3- assign b to the reminder of divide t by b
  meaning  b = 36 % 24  =>  12
--state =>  a = 24 , b = 12
  1- assign t to a   meaning t = 24
  2- assign a to b   meaning a = 12
  3- assign b to the reminder of divide t by b
  meaning  b = 24 % 12  =>  0
--state => a = 12 , b = 0
Now we return the a   which is 12
```
</details>
<details>
    <summary><strong>Measuring algorithm performance</strong></summary>
    <strong>Algorithm Performance</strong>
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
    are used to organization information in various ways so that it can be efficiently operated on by algorithms
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
    <br>
     a collection of elements, where each item is identified by an index or key data structure is a collection with defined way of accessing and sorting items
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
    is a linear collection of data elements called nodes contain reference to the next node in the list Hold whatever data the application needs
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
    <strong>node:contains data and a pointer to the next node the first item you add to the list called the head</strong>
    <br>
    <br>
    <strong>singly linked list:</strong>each item has point to the next item in the list
    <br>
    <strong>Doubly linked list::</strong> each item in the list has two pointers to the next and previous element</details>
<details>
    <summary><strong>Stacks and queues</strong></summary>
    <strong>Stacks</strong>
    <br>
    <ul>
        <li>Stack: Collection that supports push and pop operation</li>
        <li>The Last item pushed is the first one popped</li>
        <li>last in first out</li>
        <li>It follow the  LIFO  rule </li>
    </ul>
    <br>
    ٍtacks are great for programs where you need to reverse things
    <br>
    Stacks are also good for keeping track of state as things are pushed on and popped off the stacks
    <br>
    <strong>Queues</strong>
    <br>
    <ul>
        <li>Queue: Collection that supports adding and removing</li>
        <li>First item added is the first item out</li>
        <li>first in first out </li>
        <li>follow FIFO  rule </li>
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
    <strong>Hash tables</strong> associative arrays
    <br>
    it's a data structure that maps keys to their associated values, and it does this using what's calle a hash function, this function uses the key to compute an index into the slots that are in the hash table and map the key to the value
    <br>
    <strong>Hash Tables Advantages</strong>
    <br>
    <ul>
        <li>Every item have a key</li>
        <li>Key-to-value mappings are unique</li>
        <li>Hash tables are typically very fast</li>
        <li>For small datasets, arrays are usally more efficient</li>
        <li>Hash tables don't order entries in a predictable way</li>
        <li>Keys are mapped to data values by using a hash to compute an index value</li>
    </ul>
    <br>
    <strong>Hash Tables Cons</strong>
    <br>
    for small datasets, arrays are usually more efficient hash tables don't order entries in predictable way

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
```
</details>

### Recursion
<details>
    <summary><strong>Understanding recursion</strong></summary>
    <strong>Recursion:</strong> is when a function call itself
    <br>
    <ul>
        <li>Recursive function need to have a breaking condition</li>
        <li>This prevents infinite loops and eventual crashes</li>
        <li>Each time the function is called, the old arguments are saved</li>
        <li>This is called the  "call stack"</li>
    </ul>
    <br>
    <img src="https://lh3.google.com/u/2/d/1ZZ042-FvI8QyrrUJVR_NKcF7N9u0dmHC=w1366-h625-iv1">
</details>
<details>
    <summary><strong>Simple recursion example</strong></summary>
    <img src="https://lh3.google.com/u/2/d/14S-f-int5Nms2aEObForQkEW03bVafCS=w1366-h441-iv1">
    <br>

```
def countdown(x):
    if x == 0:
        print("Done!")
        return
    else:
        print(x, "...")
        countdown(x-1)


# this recursion store data as stacks
countdown(5)
```
</details>
<details>
    <summary><strong>Power and factorial</strong></summary>

```
def power(num, pwr):
    # breaking condition: if we reach zero, return 1
    if pwr == 0:
        return 1
    else:
        return num * power(num, pwr-1)
        # 2 ^3
        # first  2  *  2^2
        # then 2 * 2 *2


def factorial(num):
    if (num == 0):
        return 1
    else:
        return num * factorial(num-1)


print("{} to the power of {} is {}".format(5, 3, power(5, 3)))
print("{} to the power of {} is {}".format(1, 5, power(1, 5)))
print("{}! is {}".format(4, factorial(4)))
print("{}! is {}".format(0, factorial(0)))
```
</details>

### Sorting

<details>
    <summary><strong>Overview of sorting</strong></summary>
    <strong>Sorting Data</strong>
    <br>
    <ul>
        <li>Most modern languages have sorting built in</li>
        <li>The bubble sort</li>
        <li>The Merge sort</li>
        <li>The quick sort</li>
    </ul>
</details>
<details>
    <summary><strong>The bubble sort</strong></summary>
    <strong>bubble sort</strong>
    <br>
    <ul>
        <li>Very simple to understand and implement</li>
        <li>
            Performance O(n^2)
            <ul>
                <li>for loops inside of for loops are usually n^2 </li>
            </ul>
        </li>
        <li>Other sorting algorithms are generally much better </li>
        <li>Not considered to be a practical solution </li>
    </ul>
    <br>

```

# first come into the list
# take the first two numbers and compare them
# make the smallest first
# then move to the second and the third and compare them
# make the smallest first
# and go like that until finish the list
# then start over but this time will start from the second item and so on


def bubbleSort(dataset):  # the word database refer to the list 1
    # start with the array length and decrement each time
    # mean range (9, 0,-1) the -1  refer to make it descendant
    for i in range(len(dataset)-1, 0, -1):
        # examine each item pair
        for j in range(i):
            # swap items if needed
            if dataset[j] > dataset[j+1]:
                temp = dataset[j]
                dataset[j] = dataset[j+1]  # switch the first element
                dataset[j+1] = temp  # switch the second element

        print("Current state: ", dataset)

# a function for viewing the sorting process


def main():
    list1 = [6, 20, 8, 19, 56, 23, 87, 41, 49, 53]
    print("Starting state: ", list1)
    bubbleSort(list1)
    print("Final state: ", list1)


if __name__ == "__main__":
    main()
```
<br>
<img src="https://lh3.google.com/u/2/d/1B6ikTHl_Cy3q0MZMRXlVM-EhiizZQOWT=w1366-h625-iv1">
</details>

<details>
    <summary><strong>The Merge sort</strong></summary>
    <strong>Merge sort</strong>
    <br>
    <ul>
        <li>divide-and-conquer algorithm</li>
        <li>breaks a database into individual pieces and merge them </li>
        <li>uses recursion to operate on datasets </li>
        <li>perform  well on the large sets of data </li>
        <li>in general has a performance of O(n log n) time complexity </li>
    </ul>

```


items = [6, 20, 8, 19, 56, 23, 87, 41, 49, 53]


def mergesort(dataset):
    if len(dataset) > 1:
        mid = len(dataset) // 2
        leftarr = dataset[:mid]
        rightarr = dataset[mid:]

        # recursively break down the arrays
        mergeSort(leftarr)
        mergeSort(rightarr)
        # now perform the merging
        i = 0  # index into the left array
        j = 0  # index into the right array
        k = 0  # index into merged array

        # while both arrays have content
        while i < len(leftarr) and j < len(rightarr):
            if leftarr[i] < rightarr[j]:
                dataset[k] = leftarr[i]
                i += 1
            else:
                dataset[k] = rightarr[j]
                j += 1
            k += 1

        # if the left array still has values, add them
        while i < len(leftarr):
            dataset[k] = leftarr[i]
            i += 1
            k += 1

        # if the right array still has values, add them
        while j < len(rightarr):
            dataset[k] = rightarr[j]
            j += 1
            k += 1


# test the merge sort with data
print(items)
mergesort(items)
print(items)
```
<br>
<img src="https://lh3.google.com/u/2/d/1j3TsyetgK_j3mC0DN-6tvbFfm6R6Q786=w1366-h625-iv1">
</details>

<details>
    <summary><strong>The quick sort</strong></summary>
    <strong>quick sort</strong>
    <br>
    <ul>
        <li>divide-and-conquer algorithm, like the merge sort</li>
        <li>Also uses recursion to perform sorting </li>
        <li>Generally perform  better than merge sort  </li>
        <li>in general has a performance of O(n log n) time complexity </li>
        <li>operates in place on the data</li>
        <li>Worst case is O(n^2) when data is mostly sorted already  but that isn't common</li>
    </ul>

```

# Implement a quicksort
# O(2n)

# or (n)
items = [20, 6, 8, 53, 56, 23, 87, 41, 49, 19]


def quickSort(dataset, first, last):
    if first < last:
        # calculate the split point
        pivotIdx = partition(dataset, first, last)

        # now sort the two partitions
        quickSort(dataset, first, pivotIdx-1)
        quickSort(dataset, pivotIdx+1, last)


def partition(datavalues, first, last):
    # choose the first item as the pivot value
    pivotvalue = datavalues[first]
    # establish the upper and lower indexes
    lower = first + 1
    upper = last

    # start searching for the crossing point
    done = False
    while not done:
        # advance the lower index
        while lower <= upper and datavalues[lower] <= pivotvalue:
            lower += 1

        # advance the upper index
        while datavalues[upper] >= pivotvalue and upper >= lower:
            upper -= 1

        # if the two indexes cross, we have found the split point
        if upper < lower:
            done = True
        else:
            # exchange the two values
            temp = datavalues[lower]
            datavalues[lower] = datavalues[upper]
            datavalues[upper] = temp

    # when the split point is found, exchange the pivot value
    temp = datavalues[first]
    datavalues[first] = datavalues[upper]
    datavalues[upper] = temp

    # return the split point index
    return upper


# test the merge sort with data
print(items)
quickSort(items, 0, len(items)-1)
print(items)
```
<br>
<img src="https://lh3.google.com/u/2/d/1njQ9T01jtRDSDeragm71gLlNlD95vCEg=w1366-h625-iv1">
</details>

### Searching Data
<details>
    <summary><strong>Unordered list search</strong></summary>

```
# searching for an item in an unordered list
# sometimes called a Linear search

# declare a list of values to operate on
items = [6, 20, 8, 19, 56, 23, 87, 41, 49, 53]

def find_item(item, itemlist):
    for i in range(0, len(itemlist)):
        if item == itemlist[i]:
            return i

    return None

# take O(n)  linear time of complexity   the more items in the list the more of the searching time
print(find_item(87, items))
print(find_item(250, items))
```
</details>
<details>
    <summary><strong>Ordered list search</strong></summary>

```
# searching for an item in an ordered list  sorted list
# this technique uses a binary search


items = [6, 8, 19, 20, 23, 41, 49, 53, 56, 87]


def binarysearch(item, itemlist):
    # get the list size
    listsize = len(itemlist) - 1
    # start at the two ends of the list
    lowerIdx = 0
    upperIdx = listsize

    while lowerIdx <= upperIdx:
        # calculate the middle point
        midPt = (lowerIdx + upperIdx) // 2

        # if item is found, return the index
        if itemlist[midPt] == item:
            return midPt
        # otherwise get the next midpoint
        if item > itemlist[midPt]:
            lowerIdx = midPt + 1
        else:
            upperIdx = midPt - 1

    if lowerIdx > upperIdx:
        return None


print(binarysearch(23, items))
print(binarysearch(87, items))
print(binarysearch(250, items))
```
<br>
<img src="https://lh3.google.com/u/2/d/1vz2-u1tI5e7vgfnEUQKbzMcVrs-i-DJ-=w1366-h625-iv1">

```
With a sorted list, we can perform a type of search is called a binary search. So, let's
imagine we had a list of sorted numbers, and the number that we're searching for is the number
41. To perform the binary search, we start off with two indexes at the beginning and end of
the list, and then we calculate the midpoint of the list, rounded down in case of an uneven
division, and then we check to see if that value at the midpoint is the value that we want, and if it is, then great, we return that index. Now, if the number at that index is less than the one that we're searching for, we know that we can ignore all the numbers below that index, and conversely if that number is larger than the one we're looking for, we can ignore
all the numbers above that index. So, now we calculate the new midpoint by advancing, in
this case, the lower index up the middle we just calculated, and then we compute the new
midpoint from there. So now, the lower becomes three, the upper stays where it is, and then  new midpoint becomes five, after rounding down the division. And this process repeats until we found the number which, in our example, is at index number five.
```
</details>
<details>
    <summary><strong>Determine if a list is sorted</strong></summary>

```
# determine if a list is sorted


items1 = [6, 8, 19, 20, 23, 41, 49, 53, 56, 87]
items2 = [6, 20, 8, 19, 56, 23, 87, 41, 49, 53]

def is_sorted(itemlist):
    # using the all function
    return all(itemlist[i] <= itemlist[i+1] for i in range(len(itemlist)-1))

    # using the brute force method
    # for i in range(0, len(itemlist)-1):
    #     if (itemlist[i] > itemlist[i+1]):
    #         return False
    # return True

print(is_sorted(items1))
print(is_sorted(items2))
```
</details>

### Other Algorithms
<detials>
    <summary><strong>unique filtering with hash tables</strong></summary>

```
# use hash table to filter out duplicate items
# the time complexity will be  O(n)

# define a set of items that we want to reduce duplicates
items = ["apple", "pear", "orange", "banana", "apple",
        "orange", "apple", "pear", "banana", "orange",
        "apple", "kiwi", "pear", "apple", "orange"]

# TODO:  create a hashtable to perform a filter
filter = dict()

# TODO: loop over each item and add to the hashtable
for key in items:
	filter[key] = 0

# TODO: create a set from the resulting keys in the hashtable
result = set(filter.keys())
print(result)
```
</detials>

<details>
    <summary><strong>value counting with hash tables</strong></summary>

```
# using a hashtable to count individual items
# the time complexity is O(n)

# define a set of items that we want to count
items = ["apple", "pear", "orange", "banana", "apple",
        "orange", "apple", "pear", "banana", "orange",
        "apple", "kiwi", "pear", "apple", "orange"]

# create a hashtable object to hold the items and counts
counter = dict()

# iterate over each item and increment the count for each one
for item in items:
    if item in counter.keys():
        counter[item] += 1
    else:
        counter[item] = 1

# print the results
print(counter)
```
<br>
<img src="https://lh3.google.com/u/2/d/1D98Rztw5cIIIaY06bgjMafbuz-5D6noB=w1366-h625-iv1">

</details>

<details>
    <summary><strong>find max value recursively</strong></summary>
<img src="https://lh3.google.com/u/2/d/1IOzpUdMLH612phbmLtNGTm0l3cQGFBBC=w1366-h625-iv1">
<br>

```
# use a recursive algorithm to find a maximum value


# declare a list of values to operate on
items = [6, 20, 8, 19, 56, 23, 87, 41, 49, 53]

def find_max(items):
    # breaking condition: last item in list? return it
    if len(items) == 1:
        return items[0]

    # otherwise get the first item and call function
    # again to operate on the rest of the list
    op1 = items[0]
    print(op1)
    op2 = find_max(items[1:])
    print(op2)

    # perform the comparison when we're down to just two
    if op1 > op2:
        return op1
    else:
        return op2


# test the function
print(find_max(items))
```
</details>