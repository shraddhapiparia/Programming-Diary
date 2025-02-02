# 22. Generate Parentheses
# Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.

# Example 1:
# Input: n = 3
# Output: ["((()))","(()())","(())()","()(())","()()()"]
# Example 2:
# Input: n = 1
# Output: ["()"]
 
# Constraints:
# 1 <= n <= 8

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        openB = closeB = n
        answer, combination = [], ''
        self.findCombinations(combination, openB, closeB, answer)
        return answer

    def findCombinations(self, combination, openB, closeB, answer):
        if openB == 0 and closeB == 0:
            answer.append(combination)

        elif openB == 0:
            self.findCombinations(combination+')', openB, closeB-1, answer)

        elif closeB == 0 or openB == closeB:
            self.findCombinations(combination+'(', openB-1, closeB, answer)

        else:
            self.findCombinations(combination+'(', openB-1, closeB, answer)
            self.findCombinations(combination+')', openB, closeB-1, answer)

# Above solution creates a lot of unnecessary lists since python lists are immutable. below is optimized code
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        result = []
        self.backtrack([], 0, 0, n, result)
        return result

    def backtrack(self, current, open_count, close_count, max_pairs, result):
        if len(current) == 2 * max_pairs:
            result.append(''.join(current))
            return

        if open_count < max_pairs:
            current.append('(')
            self.backtrack(current, open_count + 1, close_count, max_pairs, result)
            current.pop()

        if close_count < open_count:
            current.append(')')
            self.backtrack(current, open_count, close_count + 1, max_pairs, result)
            current.pop()
