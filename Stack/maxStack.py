class MaxStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []

    def push(self, x: int) -> None:
        self.stack.append(x)
        

    def pop(self) -> int:
        return self.stack.pop()

    def top(self) -> int:
        return self.stack[len(self.stack)-1]

    def peekMax(self) -> int:
        return max(self.stack)

    def popMax(self) -> int:
        maxElement = max(self.stack)
        maxIndex = 0
        for i in range(len(self.stack) - 1, -1, -1):
            if maxElement == self.stack[i]:
                maxIndex = i
                break
        return self.stack.pop(maxIndex)
