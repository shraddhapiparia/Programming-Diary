# 67. Add Binary
# Given two binary strings a and b, return their sum as a binary string.
# Example 1:

# Input: a = "11", b = "1"
# Output: "100"
# Example 2:

# Input: a = "1010", b = "1011"
# Output: "10101"

# Constraints:

# 1 <= a.length, b.length <= 104
# a and b consist only of '0' or '1' characters.
# Each string does not contain leading zeros except for the zero itself.

def addBinary(self, a: str, b: str) -> str:
        arev = a[::-1]
        brev = b[::-1]
        carry = 0
        out = ''
        
        # Pad the shorter string with zeros
        max_len = max(len(a), len(b))
        arev = arev.ljust(max_len, '0')
        brev = brev.ljust(max_len, '0')

        for i in range(max_len):
            val = carry
            if arev[i] == '1':
                val += 1
            if brev[i] == '1':
                val += 1

            out += str(val % 2)
            carry = val // 2

        if carry:
            out += '1'

        return out[::-1]

# Code without reverse strings
def addBinary(self, a: str, b: str) -> str:
    i, j = len(a) - 1, len(b) - 1  # Pointers for both strings
    carry = 0
    result = []

    while i >= 0 or j >= 0 or carry:
        total = carry
        if i >= 0:
            total += int(a[i])  # Add binary digit from 'a'
            i -= 1
        if j >= 0:
            total += int(b[j])  # Add binary digit from 'b'
            j -= 1
        
        # Append current bit (total % 2) and update carry (total // 2)
        result.append(str(total % 2))
        carry = total // 2

    return ''.join(result[::-1]) 
