class Solution:
    def customSortString(self, order: str, s: str) -> str:
        count = Counter(s) #tracking frequency of characters in s
        str_build = []
        for ch in order:
            if ch in count:
                str_build.append(ch * count[ch]) #to keep duplicates in check
                del count[ch] #remove the ones we have seen

        for x in count:
            str_build.append(x * count[x])

        return "".join(str_build)

        """
        Time complexity of the above is O(n)
        Space complexity of the above is O(n)

        ALTERNATIVE METHOD
        return "".join(sorted(s, key=order.find))
        the time complexity of this is O(nlogn) but that isn't bad since the word limit for s is 200
        the space complexity is O(n)
        """
