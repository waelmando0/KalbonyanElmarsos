# Find the greatest common denominator of two numbers
# using Euclid's algorithm


def gcd(a, b):
    while b != 0:
        r = a       # At this step we store a at r
        a = b       # Then make a = b
        b = r % a   # Then let b = the remainder of devision a (stored at r) by b (stored at a)
    return a        # Return r (stored at a)

# try out the function with a few examples
print(gcd(60, 96))  # should be 12
print(gcd(20, 8))   # should be 4