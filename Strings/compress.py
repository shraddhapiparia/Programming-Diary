# 443. String Compression. Given an array of characters, compress it in-place.

# The length after compression must always be smaller than or equal to the original array. Every element of the array should be a 
# character (not int) of length 1. After you are done modifying the input array in-place, return the new length of the array.

class Solution:
    def compress(self, chars: List[str]) -> int:
        count = 1
        for i in range(len(chars)-1,-1,-1):
            if i and chars[i]==chars[i-1]:
                count += 1
                chars.pop(i)
            else:
                if count>1:
                    for item in str(count)[::-1]:
                        chars.insert(i+1, item)
                    count = 1
