class Solution:
    def addDigits(self, num: int) -> int:
        while num >= 10:
            sum_of_num = 0
            while num > 0:
                digit = num % 10 #get the leftmost digit
                sum_of_num += digit
                num = num // 10 #get the other digit of the number

            num = sum_of_num #we are meant to update the num
        return num

        #time complexity - O(log(num))
        #space complexity - O(1)
