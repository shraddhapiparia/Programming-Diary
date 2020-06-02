# 225. Implement stack using queues

class MyStack:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.queue = []

    def push(self, x: int) -> None:
        """
        Push element x onto stack.
        """
        self.queue.append(x)

    def pop(self) -> int:
        """
        Removes the element on top of the stack and returns that element.
        """
        el = self.queue[len(self.queue)-1]
        self.queue = self.queue[:-1]
        return el

    def top(self) -> int:
        """
        Get the top element.
        """
        return self.queue[len(self.queue)-1]

    def empty(self) -> bool:
        """
        Returns whether the stack is empty.
        """
        return False if self.queue else True
