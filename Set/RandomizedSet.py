# 380. Insert Delete GetRandom O(1)
# Implement the RandomizedSet class:

# RandomizedSet() Initializes the RandomizedSet object.
# bool insert(int val) Inserts an item val into the set if not present. Returns true if the item was not present, false otherwise.
# bool remove(int val) Removes an item val from the set if present. Returns true if the item was present, false otherwise.
# int getRandom() Returns a random element from the current set of elements (it's guaranteed that at least one element exists when this method is called). Each element must have the same probability of being returned.
# You must implement the functions of the class such that each function works in average O(1) time complexity.

class RandomizedSet:

    def __init__(self):
        self.arr = []
        self.map = {}

    def insert(self, val: int) -> bool:
        if val not in self.map:
            self.arr.append(val)
            self.map[val] = len(self.arr) -1 
            return True
        else:
            return False
        

    def remove(self, val: int) -> bool:
        if val not in self.map:
            return False
        # swap the val with last element and pop it
        idx = self.map[val]
        l_elem = self.arr[-1]
        self.map[l_elem] = idx
        self.arr[idx] = l_elem

        # pop the element
        self.arr[-1] = val
        self.arr.pop()
        self.map.pop(val)
        return True


    def getRandom(self) -> int:
        return random.choice(self.arr)


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()
