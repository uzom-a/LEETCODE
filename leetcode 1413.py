class Solution:
    def minStartValue(self, nums: List[int]) -> int:
        startValue = 1
        
        
        while True:
            total = startValue
            is_valid = True
        
            for num in nums:
                total += num

                if total < 1 : #when our condition fails change the is_valid flag
                    is_valid = False
                    break

            if is_valid: #if the loop ended and all is well then we used the right startvalue
                return startValue
            else:
                startValue += 1
