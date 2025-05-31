class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        """
        PSEDUOCODE TIMEE
        get the minimum number in nums
        add the elements in stack in an ascending order
        if not do not add
        return the length of the stack
        """
        num_set = set(nums)
        longest = 0

        for num in num_set:
            if (num - 1) not in num_set:
                length = 1 #start the sequence 
                while (num + length) in num_set: #used to keep the sequence going
                    length += 1 
                longest = max(length, longest)

        return longest
        #Time Complexity = O(n)
        #Space Complexity = O(n)  

        
        """
        THIS LIMITS THE STARTING ELEMENT TO BE THE MINIMUM
        minn = min(nums)
        stack = []
        stack.append(minn)

        for num in nums:
            if num == minn +1:
                stack.append(num)
                minn = num
            
        print(stack)
        return len(stack)
        """
