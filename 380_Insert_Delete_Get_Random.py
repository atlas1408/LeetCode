import random
class RandomizedSet:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.map = {}
        self.arr = []        

    def insert(self, val: int) -> bool:
        """
        Inserts a value to the set. Returns true if the set did not already contain the specified element.
        """
        if val not in self.map:
            self.arr.append(val)
            self.map[val] = len(self.arr)-1
            return True
        return False
        

    def remove(self, val: int) -> bool:
        """
        Removes a value from the set. Returns true if the set contained the specified element.
        """
        if val in self.map:
            index = self.map[val]
            temp = self.arr[-1]
            self.arr[index], self.arr[-1] = self.arr[-1], self.arr[index]
            self.map[temp] = index
            self.arr.pop()
            del self.map[val]
            return True
        return False

    def getRandom(self) -> int:
        """
        Get a random element from the set.
        """
        return random.choice(self.arr)
        


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()