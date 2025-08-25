import random


class RandomizedSet:

    def __init__(self):
        self.arr = []
        self.set = {}

    def insert(self, val: int) -> bool:
        if val in self.set:
            return False
        self.arr.append(val)
        self.set[val] = len(self.arr) - 1
        return True

    def remove(self, val: int) -> bool:
        if val in self.set:
            # data retrival
            val_index = self.set[val]
            last_val = self.arr[-1]
            # swap
            self.arr[-1], self.arr[val_index] = self.arr[val_index], self.arr[-1]
            # clean up
            self.set[last_val] = val_index
            # removal
            self.arr.pop()
            self.set.pop(val)
            return True
        return False

    def getRandom(self) -> int:
        return random.choice(self.arr)


# Your RandomizedSet object will be instantiated and called as such:
obj = RandomizedSet()
param_1 = obj.insert(1)
param_2 = obj.remove(2)
param_3 = obj.getRandom()
