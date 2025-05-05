class Solution:
    def getAverages(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        size = 2 * k + 1

        avgs = [-1] * n
            
        #BASE CASES
        if k == 0:
            return nums
        
        if size > n :
            return avgs
        
        #CREATE PREFIX SUM
        prefix = [nums[0]]
        for i in range(1, n):
            prefix.append(nums[i] + prefix[-1])
            
        #SOLUTION SOLUTION
        for i in range(k, n-k):  #range(k, n-k) is the place where you would find valid indices
            if i == k:
                avgs[i] = prefix[i+k] // size 
            else:
                subarraySum = prefix[i+k] - prefix[i-k-1]
                avgs[i] = subarraySum // size
            
        return avgs    
            
        
