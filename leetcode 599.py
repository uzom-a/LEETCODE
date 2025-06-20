class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        i = 0
        j = 0
        minn = float('inf')
        res = []
        d = {}

        for i, word in enumerate(list1):
            d[word] = i

        for i, word in enumerate(list2):
            if word in d and i + d[word] < minn:
                    minn = min(minn, i + d[word])
                    res.clear()
                    res.append(word)
            elif word in d and i + d[word] == minn:
                    minn = min(minn, i + d[word])
                    res.append(word)
        
        return res
