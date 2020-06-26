# 232. Implement Queue using Stacks. Implement the following operations of a queue using stacks.
#    push(x) -- Push element x to the back of queue.
#    pop() -- Removes the element from in front of queue.
#    peek() -- Get the front element.
#    empty() -- Return whether the queue is empty.

# Below solution is not correct since it is treating stack as lists

class MyQueue:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.stack = []

    def push(self, x: int) -> None:
        """
        Push element x to the back of queue.
        """
        self.stack.append(x)

    def pop(self) -> int:
        """
        Removes the element from in front of queue and returns that element.
        """
        val = self.stack[0]
        self.stack = self.stack[1:]
        return val

    def peek(self) -> int:
        """
        Get the front element.
        """
        return self.stack[0]

    def empty(self) -> bool:
        """
        Returns whether the queue is empty.
        """
        return True if not self.stack else False
        
# Use approach below

class MyQueue:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.stack1 = []
        self.stack2 = []

    def push(self, x: int) -> None:
        """
        Push element x to the back of queue.
        """
        self.stack1.append(x)

    def pop(self) -> int:
        """
        Removes the element from in front of queue and returns that element.
        """
        for i in range(len(self.stack1)):
            self.stack2.append(self.stack1.pop())
        val = self.stack2.pop()
        for i in range(len(self.stack2)):
            self.stack1.append(self.stack2.pop())
        return val

    def peek(self) -> int:
        """
        Get the front element.
        """
        return self.stack1[0]

    def empty(self) -> bool:
        """
        Returns whether the queue is empty.
        """
        return True if not self.stack1 else False
