
# when it comes at the recursion point
# the interpitter didnt move to the next line,
# it's got into the fun again and start over and over
# till it done, then back to finish it

def countdown(x):
    if x == 0:
        print("Done!")
        return
    else:
        print(x, "...")
        countdown(x-1)
        print("yooh!")


countdown(5)