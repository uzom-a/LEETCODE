class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        operations = 0

        for num in nums:
            if num % 3 == 0:
                continue
            else:
                if(num+1) % 3 == 0:
                    operations += 1
                else:
                    if(num-1) % 3 == 0:
                        operations += 1

        return operations

        #Time complexity : O(n)
        #Space Complexity : O(1)
