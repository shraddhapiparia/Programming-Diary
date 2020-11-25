# 227. Basic Calculator II
# Implement a basic calculator to evaluate a simple expression string.

# The expression string contains only non-negative integers, +, -, *, / operators and empty spaces . The integer division should truncate toward zero.

class Solution:
    def calculate(self, s: str) -> int:
        stack = []
        operators = {'+','-','*','/'}
        sign = '+'
        tmp = 0
        for i in range(len(s)):
            letter = s[i]
            if letter not in operators and letter != ' ':
                tmp = tmp*10 + int(letter)
            if letter in operators or i == len(s)-1:
                if sign == '+':
                    stack.append(tmp)
                if sign == '-':
                    stack.append(-tmp)
                if sign == '*':
                    tmp = tmp*stack.pop()
                    stack.append(tmp)
                if sign == '/':
                    vertex = stack.pop()
                    if vertex > 0:
                        stack.append(vertex//tmp)
                    else:
                        stack.append(-1*((-vertex)//tmp))
                sign = letter
                tmp = 0
        return sum(stack)

