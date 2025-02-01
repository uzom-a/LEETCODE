class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        if len(nums) == 2: #base case
            return nums

        m = len(nums)
        result = []
        first = 0
        second = m //2 

        for first in range(m // 2):
            result.append(nums[first])
            if second < m:
                result.append(nums[second])
                second += 1
        
        return result

        """
        U-Understand
        make the "coordinates" come together and return the list

        M-Match:
        two pointers, array

        P-Plan
        create result list
        first pointer starts at the first element
        second pointer starts at the (n + 1) element
        iterate through array 
        append to the result list while alternate between the first element and the second element
        return result

        I-Implement
        Look at the code above

        R-Review

        E-Evaluate
        Time Complexity = O(n)
        Space Complexity = O(n)

        """
