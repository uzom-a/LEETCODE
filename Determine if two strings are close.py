from collections import Counter
class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        if len(word1) != len(word2):
            return False

        #I think operation 1 means sorting

        if sorted(word1) == sorted(word2):
            return True

        count1 = Counter(word1)
        count2 = Counter(word2)
        #print(count1.values()) the order of this would be different from the next so I have to sort
        #print(count2.values()) the order of this would be different from the next so I have to sort

        if set(count1.keys()) != set(count2.keys()): #the number of unique characters have to be equal for that bijection to work
            return False

        if sorted(count1.values()) == sorted(count2.values()):
            return True
        else:
            return False

#Time complexity = O(nlogn)
#Space Complexity = O(n)

        
