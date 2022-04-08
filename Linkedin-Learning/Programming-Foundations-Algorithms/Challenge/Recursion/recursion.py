
def power(num, pwr):
    # breaking condition: if we reach zero, return 1
    if pwr == 0:
        return 1
    else:
        return num * power(num, pwr-1)
        # 5 (pwr=2) * 5 (pwr=1) * 5 (pwr=0) * 1 = 125

def factorial(num):
    if (num == 0):
        return 1
    else:
        return num * factorial(num-1)
        # 5 (num=4) * 4 (num=3) * 3 (num=2) * 2 (num=1) * 1 (num=0) * 1 = 120


print("{} to the power of {} is {}".format(5, 3, power(5, 3)))
print("{} to the power of {} is {}".format(1, 5, power(1, 5)))
print("{}! is {}".format(5, factorial(5)))
print("{}! is {}".format(0, factorial(0)))