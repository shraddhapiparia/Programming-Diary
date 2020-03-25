class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str: 
        if not strs:
            return ""
        l = len(strs[0])
        for i in range(len(strs)):
            l = len(strs[i]) if len(strs[i]) < l else l
        for i in reversed(range(l)):
            pre = strs[0][:i+1]
            count = 0
            for s in strs:
                if pre == s[:i+1]:
                    count += 1
            if count == len(strs):
                return pre 
        return ""
