import time

startTime = time.time()

# defines a SuperStack that has various methods
class SuperStack:

    # initializes an emplty stack (list) on creation of instance
    def __init__(self):
        self.stack=[]

    # adds an element to the top of the stack and prints the top element
    def push(self, x: int) -> None:
        self.stack.append(x)
        print(self.stack[-1])

    # deletes the top element from the stack and prints the new top element
    def pop(self) -> int:
        self.stack.pop()
        print(len(self.stack) > 0 and self.stack[-1] or "EMPTY")

    # increments the bottom i elements of the stack by v 
    def inc(self, i: int, v: int) -> None:
        for x in range(min(i, len(self.stack))):
            self.stack[x]=self.stack[x]+v
        print(len(self.stack) > 0 and self.stack[-1] or "EMPTY")

# creates an instance of SuperStack class 
ss = SuperStack()

no_of_operations = int(input())

operations = []

# takes multiple commands from user
for i in range(no_of_operations):
    command = input()
    operations.append(command)

# separates each input command into operation and arguments and execute them
for command in operations:
    operation, *args = command.split(" ")
    args = [int(i) for i in args]
    getattr(ss, operation)(*args)

endTime = time.time()

# prints the time taken for execution
print(endTime - startTime)
