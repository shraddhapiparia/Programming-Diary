# 155. Min Stack
# Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.
# Implement the MinStack class:
# MinStack() initializes the stack object.
# void push(int val) pushes the element val onto the stack.
# void pop() removes the element on the top of the stack.
# int top() gets the top element of the stack.
# int getMin() retrieves the minimum element in the stack.
# You must implement a solution with O(1) time complexity for each function.

# Example 1:
# Input
# ["MinStack","push","push","push","getMin","pop","top","getMin"]
# [[],[-2],[0],[-3],[],[],[],[]]
# Output
# [null,null,null,null,-3,null,0,-2]
# Explanation
# MinStack minStack = new MinStack();
# minStack.push(-2);
# minStack.push(0);
# minStack.push(-3);
# minStack.getMin(); // return -3
# minStack.pop();
# minStack.top();    // return 0
# minStack.getMin(); // return -2

# Constraints:
# -231 <= val <= 231 - 1
# Methods pop, top and getMin operations will always be called on non-empty stacks.
# At most 3 * 104 calls will be made to push, pop, top, and getMin.

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

# Solution in O(1) time:

class MinStack:
    def __init__(self):
        self.stack = []
        self.min_stack = []       

    def push(self, val: int) -> None:
        self.stack.append(val)
        if not self.min_stack or val <= self.min_stack[-1]:
            self.min_stack.append(val)
        else:
            self.min_stack.append(self.min_stack[-1])
        
    def pop(self) -> None:
        if self.stack:
            self.stack.pop()
            self.min_stack.pop()
            
    def top(self) -> int:
        return self.stack[-1]      

    def getMin(self) -> int:
        return self.min_stack[-1]
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
