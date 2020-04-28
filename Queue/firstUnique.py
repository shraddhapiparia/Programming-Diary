class FirstUnique:

    def __init__(self, nums: List[int]):
        self.dict = collections.OrderedDict()
        for num in nums:
            self.dict[num] = self.dict[num] + 1 if num in self.dict else 1
                

    def showFirstUnique(self) -> int:
        for item in self.dict:
            if self.dict[item] == 1:
                return item
        return -1
        

    def add(self, value: int) -> None:
        self.dict[value] = self.dict[value] + 1 if value in self.dict else 1
        
# You have a queue of integers, you need to retrieve the first unique integer in the queue.
# Implement the FirstUnique class:

   # FirstUnique(int[] nums) Initializes the object with the numbers in the queue.
   # int showFirstUnique() returns the value of the first unique integer of the queue, and returns -1 if there is no such integer.
   # void add(int value) insert value to the queue.
# Input: 
# ["FirstUnique","showFirstUnique","add","showFirstUnique","add","showFirstUnique","add","showFirstUnique"]
# [[[2,3,5]],[],[5],[],[2],[],[3],[]]
# Output: 
# [null,2,null,2,null,3,null,-1]
