class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        str_num = str(n)
        list_version = list(str_num)
        s = 0
        p = 1 #you cannot initialize to 0 because anything times 0 is 0

        for num in list_version:
            s += int(num)


        for num in list_version:
            p *= int(num)


        return p - s

        """
        R-review 
        this is such a brute force method

        E-Evaluate
        Time Complexity: O(n)
        Space Complexity: O(n)
        """
