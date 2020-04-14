# Perform String Shifts
'''You are given a string s containing lowercase English letters, and a matrix shift, where shift[i] = [direction, amount]:

    direction can be 0 (for left shift) or 1 (for right shift). 
    amount is the amount by which string s is to be shifted.
    A left shift by 1 means remove the first character of s and append it to the end.
    Similarly, a right shift by 1 means remove the last character of s and add it to the beginning.

Return the final string after all operations.'''

class Solution:
    def stringShift(self, s: str, shift: List[List[int]]) -> str:
        newstr, count = '', 0
        for lst in shift:
            d, amt = lst
            count = count + amt if d == 0 else count - amt
        count %= len(s)
        new =  s[count:] + s[:count]
        return new
