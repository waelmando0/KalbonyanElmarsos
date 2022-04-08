from collections import deque

# TODO: create a new empty deque object that will function as a queue

queue = deque()

# TODO: add some items to the queue

queue.append('a')
queue.append('b')
queue.append('c')
queue.append('d')

# TODO: print the queue contents

print(queue)
x = queue.popleft()
print(x)
print(queue)

# TODO: pop an item off the front of the queue
