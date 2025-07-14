#NEXT GREATER ELEMENT

class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        stack = []
        ans = [0] * len(nums1)
        
        for i in range(len(nums1)):
            stack.clear()
            j = 0
            
            while j < len(nums2):
                if nums1[i] == nums2[j]:
                    break #leave this while loop and move to the next step
                    
                j += 1
                    
            #dealing with finding the next greater element
            j += 1
            while j < len(nums2):
                    if nums2[j] > nums1[i]:
                        stack.append(nums2[j])
                        break
                    else:
                        stack.append(nums2[j])
                    j += 1
                    
            #once we find a greater element and we get to this stage then it is time to put it in the ans array
            if stack and stack[-1] > nums1[i]:
                ans[i] = stack[-1]
            else:
                ans[i] = -1
                
        return ans
    """
    SPACE COMPLEXITY = O(m)
    TIME COMPLEXITY = O(n x m ) where n is the length of nums1 and m is the length of nums2
    """
    #a smarter way to do this is to find the next greater element for each element in nums2 and store in a dictionary
    #while still using the montonic decreasing stack technique and then for the elments in nums1 check the hash map 
    #for its next greater element chikena