class Solution:
    def isPalindrome(self, x: int) -> bool:
        n = len(str(x))

        while x and n > 1 #n cannot become 0 unless the code will break:
            right = x % 10
            left = x // 10**(n-1)

            if left != right:
                return False

            x = x % 10**(n-1)  #remove the left digit
            x = x // 10   #remove the right digit and update
            
            n = n - 2

        return True



"""
       if x < 0:
        return False

        div = 1
        while x >= 10 * div:   #creating the divisor
            div *= 10

        while x:
            right = x % 10
            left = x // div

            if left != right:
                return False

            x = (x % div) // 10
            div = div / 100   #chop off two digits for the next x
        return True

"""

            
