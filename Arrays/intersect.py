class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        dicti, out = {}, []
        for n1 in nums1:
            dicti[n1] = dicti[n1] + 1 if n1 in dicti else 1
        for n2 in nums2:
            if n2 in dicti and dicti[n2] > 0:
                out.append(n2)
                dicti[n2] -= 1
        return out
