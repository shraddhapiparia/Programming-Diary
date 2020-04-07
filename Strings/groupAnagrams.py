class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dicti = {} 
        for str in strs: 
            key = ''.join(sorted(str))
            if key not in dicti: 
                dicti[key] = [str]
            else: 
                dicti[key].append(str)
        return dicti.values()
        
        
# 49. Group Anagrams. Given an array of strings, group anagrams together.
