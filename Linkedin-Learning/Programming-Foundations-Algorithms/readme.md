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
    2. If the remainder, r is 0 then stop: GCD is b
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