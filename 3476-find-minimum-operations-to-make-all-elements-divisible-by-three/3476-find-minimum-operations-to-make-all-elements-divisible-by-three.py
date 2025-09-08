class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        """
        PSEUDOCODE
        -init operations
        -traverse the list
        -if num % 3 != 0:
        -if even:
        -   add 1
        -   increment operations
        -if odd:
        -   subtract 1 
        -   increment operations
        """
        operations = 0
        for num in nums:
            if num % 3 != 0:
                if num % 2 == 0:   #even
                    operations += 1
                else:
                    operations += 1

        return operations

        #Time Complexity Worst Case: O(n)
        #Space Complexity: O(1)

