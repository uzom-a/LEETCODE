class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        n = len(nums)
        left = [0] * n
        add = 0
        

        for i in range(1, len(nums)):  #find the left sum for each index
            left[i] = left[i-1] + nums[i-1] #the left is doing the main addition job the nums is just adding that current number to the former sum
        print(left)

        right = [0] * n
        add2 = 0
        

        for i in range(n-2, -1, -1): #find the right sum for each index from the back
            right[i] = right[i+1] + nums[i+1]
        print(right)

        for i in range(len(right)):  #compare each index in the two arrays
            if left[i] == right[i]:
                return i 

        #leaving that for loop above will mean there is no pivot index
        return -1
