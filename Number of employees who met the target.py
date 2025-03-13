class Solution:
    def numberOfEmployeesWhoMetTarget(self, hours: List[int], target: int) -> int:
        count = 0
        for num in hours:
            if num >= target:
                count += 1  #employee works AT LEAST hours

        return count

    #Time complexity : O(n)
    #Space Complexity: O(1)
