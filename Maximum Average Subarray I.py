class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        n = len(nums)
        total = sum(nums[i] for i in range(k)) #get the intial sum of the numbers in the range
        maximum = total

        for i in range(n - k):
            total += nums[i + k] - nums[i] #add the next element and remove the first element
            maximum = max(maximum, total)

        return maximum / k
            
    """
        U-Understand
        we need to find the new 4 contiguous numbers that result in the maximum average value

        M-Match
        sliding window, array

        P-Plan
        get the sum of first k 
        then remove i and add i + k to the next window
        stop whenn i + k cannot go further
        return maximum average value

        I-Implement
        Check above

        R-Review

        E-Evaluate
        Time Complexity : O(n)
        Space Complexity : O(1)

    """

#I UNDERSTAND THIS CODE BELOW FR 
class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        curr = 0
        
        for i in range(k):
            curr += nums[i] #generate the sum for the first fixed window
            
        ans = curr / k
        
        for i in range(k, len(nums)):    #continue with the rest of the array
            curr += nums[i] - nums[i-k] # increasing and decreasing the size of the fixed window
            
            ans = max(ans, (curr / k))

        return ans
            
        
        
