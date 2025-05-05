class Solution:
    def reverseOnlyLetters(self, s: str) -> str:
        #two pointer approach would work we just have to skip non english letters

        #INTIALIZE VARIABLES 
        n = len(s)
        left = 0
        right = n - 1
        s_list = list(s)

        #LOOP THROUGH THE LIST
        while left < right:
            if s_list[left].isalpha() and s_list[right].isalpha():
                s_list[left], s_list[right] = s_list[right], s_list[left]
                left += 1
                right -= 1
            if not s_list[left].isalpha():
                left += 1
            if not s_list[right].isalpha():
                right -= 1

        return ''.join(s_list)
