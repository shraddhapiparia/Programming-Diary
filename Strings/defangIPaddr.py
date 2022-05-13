# 1108. Defanging an IP Address. Given a valid (IPv4) IP address, return a defanged version of that IP address. Easy

# A defanged IP address replaces every period "." with "[.]".

# Example 1:

# Input: address = "1.1.1.1"
# Output: "1[.]1[.]1[.]1"

class Solution:
    def defangIPaddr(self, address: str) -> str:
        new = ""
        for i in range(len(address)):
            if address[i] == '.':
                new += '[.]'
            else:
                new += address[i]
        return new
    
 # One liner

class Solution:
    def defangIPaddr(self, address: str) -> str:
        return address.replace('.','[.]')
