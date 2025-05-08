class Solution:
    def countElements(self, arr: List[int]) -> int:
        count = 0
        
        for x in arr:
            if (x+1) in arr:
                count += 1
                
        return count

#the time complexity is terrible tho O(n^2) because inside each loop checking for the existence of an element is O(n) in itself

#space complexity = O(1)

#BETTER SOLUTION

class Solution:
    def countElements(self, arr: List[int]) -> int:
        hash_set = set(arr)
        count = 0
        for x in arr: #loop over the array because the array would contain duplicates
            if x + 1 in hash_set: #using the hash set optimizes the run time of each operation in the for loop to O(1) instead of O(n)
                count += 1
        return count

#Time Complexity: O(n)
#Space Complexity: O(n)
