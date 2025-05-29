class Solution:
    def findLucky(self, arr: List[int]) -> int:
        """
        PSEUDOCODE TIMEE
        initialize a counter for the arr
        initialize ans
        iterate through the dictionary and check if the frequency is equal to the number itself
        if yes, store the maximum as you iterate
        return ans if there is one 
        if not return -1
        """

        count = Counter(arr)
        ans = 0

        for key, value in count.items():
            if key == value:
                ans = max(ans,key)

        return ans if ans else -1

        "time complexity = o(n) because you have to iterate through the dictionary to find the  lucky integer"
        "space complexity = O(n) because the dictionary stores n integers"
