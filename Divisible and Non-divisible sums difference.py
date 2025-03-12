class Solution:
    def differenceOfSums(self, n: int, m: int) -> int:
        num1list = []
        for num in range(1, n+1):
            if num % m != 0:
                num1list.append(num)

        num2list = []  
        for num in range(1, n+1):
            if num % m == 0:
                num2list.append(num)

        num1 = sum(num1list)
        num2 = sum(num2list)

        return num1 - num2
        #time complexity: O(n)
        #Space Complexity = O(n)
