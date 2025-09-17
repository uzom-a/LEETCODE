class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:

    # FORMULA: curr_sum - k = prefix_sum[i]
    # and of we have seen that before then that subarray definitely equals to k
    # prefix_sum has to start with 0 and sum of nums[i:j] would work in the case that j is exclusive

        prefix_sum = [0]

        #Build prefix_sum
        for i in range(len(nums)):
            prefix_sum.append(nums[i] + prefix_sum[-1])

        #build hash map
        seen = {0:1}

        #iterate through nums
        curr_sum = 0
        count = 0
        for i in range(len(nums)):
            curr_sum += nums[i]
            if (curr_sum - k) in seen:
                count += seen.get(curr_sum - k, 0)

            if curr_sum in seen:
                seen[curr_sum] += 1 #the hashmap is keeping track of the prefix_sums so that is why we are storing current_sum in the hashmap
            else:
                seen[curr_sum] = 1

        return count

#Time Complexity = O(n)
#Space Complexity = O(n)