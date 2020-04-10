class Solution:
    def backspaceCompare(self, S: str, T: str) -> bool:
        s = t = ''
        count = 0
        for i in reversed(range(len(S))):
            if S[i] != '#' and count == 0:
                s += S[i]
            elif S[i] != '#' and count > 0:
                count -= 1
            else:
                count += 1
        count = 0
        for i in reversed(range(len(T))):
            if T[i] != '#' and count == 0:
                t += T[i]
            elif T[i] != '#' and count > 0:
                count -= 1
            else:
                count += 1
        return s == t
        
# Given two strings S and T, return if they are equal when both are typed into empty text editors. # means a backspace character.
