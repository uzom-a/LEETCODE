from collections import Counter
class Solution:
    def minSteps(self, s: str, t: str) -> int:
        """
        PSEUDOCODE
        count the alphabets in s and t and store in a dict
        if element in dict_t not in s:
            increment count
        else:
            if unequal increment count
        return count
        """

        steps = 0
        count_s = Counter(s)
        count_t = Counter(t)

        for ch in count_s:
            if count_s[ch] > count_t[ch]:
                steps += count_s[ch] - count_t[ch]

        return steps
