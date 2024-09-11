190. Reverse Bits
Reverse bits of a given 32 bits unsigned integer.
  Example 1:

Input: n = 00000010100101000001111010011100
Output:    964176192 (00111001011110000010100101000000)
Explanation: The input binary string 00000010100101000001111010011100 represents the unsigned integer 43261596, so return 964176192 which its binary representation is 00111001011110000010100101000000.

class Solution:
    def reverseBits(self, n: int) -> int:
        nstr = '{:032b}'.format(n)
        rev = nstr[::-1]
        reversed_bits = int(rev, 2)
        
        return reversed_bits

# Similar solution
class Solution:
    def reverseBits(self, n: int) -> int:
        n = format(n, 'b')
        n = n.zfill(32)

        return int(n[::-1], 2)


# One liner
def reverseBits(self, n: int) -> int:
    return int(format(n, 'b').zfill(32)[::-1], 2)
