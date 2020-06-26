# 20. Valid Parentheses. Given a string containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

# An input string is valid if : (1) Open brackets must be closed by the same type of brackets.
#    (2) Open brackets must be closed in the correct order.

# Note that an empty string is also considered valid.

class Solution:
    def isValid(self, s: str) -> bool:
        h = {")": "(","}": "{","]":"["}
        stack = []
        if not s:
            return True
        for i in s:
            if i in h:
                if stack and h[i] == stack[len(stack)-1]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(i)  
        return True if not stack else False
