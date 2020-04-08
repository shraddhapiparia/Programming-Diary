class Solution:
    def countElements(self, arr: List[int]) -> int:
        dicti, summ = {}, 0
        for n in arr:
            if n not in dicti:
                dicti[n] = 1
            else:
                dicti[n] += 1
        for key,val in dicti.items():
            if key-1 in dicti:
                summ += dicti[key-1]
        return summ
# O(N)
