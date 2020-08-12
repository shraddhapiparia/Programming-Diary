# 379. Design Phone Directory
# Design a Phone Directory which supports the following operations:
#    get: Provide a number which is not assigned to anyone.
#    check: Check if a number is available or not.
#    release: Recycle or release a number.


class PhoneDirectory:

    def __init__(self, maxNumbers: int):
        """
        Initialize your data structure here
        @param maxNumbers - The maximum numbers that can be stored in the phone directory.
        """
        self.s = set(range(maxNumbers))

    def get(self) -> int:
        """
        Provide a number which is not assigned to anyone.
        @return - Return an available number. Return -1 if none is available.
        """
        return self.s.pop() if self.s else -1

    def check(self, number: int) -> bool:
        """
        Check if a number is available or not.
        """
        return True if number in self.s else False
            

    def release(self, number: int) -> None:
        """
        Recycle or release a number.
        """
        self.s.add(number)

