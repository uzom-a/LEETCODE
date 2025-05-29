class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        """
        PSEUDOCODE TIMEE
        intialize a counter for the arr
        make a list of the dictionary's values
        if the set of the list has the same length as the list 
            return True
        else 
            return False
        """

        count = Counter(arr)

        list_val = list(count.values())

        seen = set(list_val)

        if len(seen) == len(list_val):
            return True
        else:
            return False

        """
        Time complexity = O(n)
        Space Complexity is O(n)
        """
