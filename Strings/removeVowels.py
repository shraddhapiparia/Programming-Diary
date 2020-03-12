class Solution:
    def removeVowels(self, S: str) -> str:
        vow = "aeiou"
        if len(S) == 0:
            return None
        return ''.join(S[i] for i in range(len(S)) if S[i] not in vow)
