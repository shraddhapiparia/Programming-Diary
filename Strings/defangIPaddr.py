# 1108. Defanging an IP Address. Given a valid (IPv4) IP address, return a defanged version of that IP address.

# A defanged IP address replaces every period "." with "[.]".

class Solution:
    def defangIPaddr(self, address: str) -> str:
        new = ""
        for i in range(len(address)):
            if address[i] == '.':
                new += '[.]'
            else:
                new += address[i]
        return new
