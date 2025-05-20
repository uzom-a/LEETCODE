class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        count = 0
        dup = defaultdict(list)
        dup[0] = [0] #usually start prefix sum with a dummy zero so add it to the dic 
        max_len = 0
        
        for i, x in enumerate(nums, 1): #if doing prefix sum no need to start from the first element
            count += x or -1
            if len(dup[count]) < 2:
                dup[count].append(i)
            if len(dup[count]) == 2:
                dup[count][1] = max(dup[count][1], i)
                max_len = max(max_len, dup[count][1]-dup[count][0])
                
        return max_len

#Time Complexity is O(n)
#Space Complexity is O(n)
# Note time complexity of the max built in function returns O(1) when it is only comparing two numbers if it is comparing in an iterable then it is O(n)
