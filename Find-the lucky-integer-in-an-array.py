class Solution:
    def findLucky(self, arr: List[int]) -> int:
        d = {}
        for i in range(len(arr)):
            if arr[i] not in d: 
                d[arr[i]] = 1
            else:
                d[arr[i]] += 1

        maximum = float('-inf')
        print(d)

        for key, value in d.items():
            if key == value:
                maximum = max(key, maximum) #this is because we need the largest lucky integer
                
            else:
                maximum = max(-1, maximum)
        
        return maximum

        """
        Time Complexity - O(n)
        Space Complexity - O(n)
        """
