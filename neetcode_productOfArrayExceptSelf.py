class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = []
        i = 0
        j = 0
        n = len(nums)

        product = 1
        prefix = [1] * n #there is no elements before the first element so set thee first element to 1
        for i in range(1,len(nums)):
            prefix[i] *= prefix[i-1] * nums[i-1] #multiply the previous elements

        product = 1
        suffix = [1] * n #set values for the entire array
        suffix[n-1] = 1 
        for i in range(len(nums)-2, -1, -1): #For the last element (i = n-1), there are no elements to the right of it. So, by definition, suffix[n-1] = 1 (the neutral element for multiplication).
            suffix[i] *= suffix[i+1] * nums[i+1]

        for i in range(len(prefix)):
            answer = prefix[i] * suffix[i]
            res.append(answer)

        return res
            
