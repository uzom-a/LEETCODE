class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        """
        PSEUDOCODEE
        -build a list of numbers from [0,n]
        -convert the input nums list to  a set
        -iterate through the list of numbers and check if it is in the set
        -if not, return that number
        -if the array is over then return None 
        """
        n = len(nums)
        helperList = []
        for i in range(n+1):
            helperList.append(i)

        input_set = set(nums)
        for num in helperList:
            if num not in input_set:
                return num

        return None