from collections import defaultdict
class RandomizedSet:

    def __init__(self):
        self.listt = []
        self.dictt = defaultdict()
        self.len = 0

    def insert(self, val: int) -> bool:
        if val in self.dictt:
            return False

        self.listt.append(val)
        self.dictt[val] = self.len
        self.len += 1

        return True #this line has to work regardless because if it was present it woul dhave failed in line 11

    def remove(self, val: int) -> bool:
        if not val in self.dictt:
            return False

        last_element = self.listt[-1]
        ind = self.dictt[val]


#Swap the current value with the last_element
        self.listt[ind] , self.dictt[last_element] = last_element, ind

        #Pop the last element (which was a duplicate after the swap).Remove val from the dictionary.

        self.listt.pop()
        del self.dictt[val]
        self.len -= 1
        return True

    def getRandom(self) -> int:
        return random.choice(self.listt)


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()