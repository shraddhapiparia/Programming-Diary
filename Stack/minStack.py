class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []

    def push(self, x: int) -> None:
        self.stack.append(x)

    def pop(self) -> None:
        self.stack.pop()

    def top(self) -> int:
        return self.stack[len(self.stack)-1]

    def getMin(self) -> int:
        return min(self.stack)
        '''mini = math.inf
        for i in range(len(self.stack)-1,-1,-1):
            if self.stack[i] < mini:
                mini = self.stack[i]
        return mini'''


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()


#Order of 1 for getmin

class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.items = []
        self.min = []

    def push(self, x: int) -> None:
        self.items.append(x)
        if not self.min or x <= self.min[-1]:
            self.min.append(x)

    def pop(self) -> None:
        if not self.items:
            return None
        
        item = self.items.pop()
        
        if item == self.min[-1]:
            self.min.pop() 
        
        return item 
    
    def top(self) -> int:
        if not self.items:
            return None
        return self.items[-1]

    def getMin(self) -> int:
        if not self.min: 
            return None
        return self.min[-1]
