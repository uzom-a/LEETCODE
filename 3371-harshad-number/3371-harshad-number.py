class Solution:
    def sumOfTheDigitsOfHarshadNumber(self, x: int) -> int:
        if x == 100:
            return 1

        unit = x % 10
        ten = x // 10

        summ = unit + ten

        if x % summ == 0 :
            return summ
        else:
            return -1

        #Space and Time Complexity of O(1)