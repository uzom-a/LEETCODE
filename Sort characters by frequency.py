class Solution:
    def frequencySort(self, s: str) -> str:
        """
        PSEUDOCODE TIMEE
        intialize a counter for the string
        sort the dictionary by the frequency in decreasing order
        append the keys from the sorted dictionary to a list
        turn the list to a string
        """

        count = Counter(s)
        res = []

        sorted_d = dict(sorted(count.items(), key=lambda item: item[1], reverse=True))

        for key, value in sorted_d.items(): 
            while value:
                res.append(key)
                value -= 1

        return ''.join(res)

        """
        Time Complexity = O(nlogn). on a regular it would b klogk for k representung unique characters but in the worst case that the frequency is 1 for each character then my time complexity is correct
        Space Complexity = O(n)
        """
