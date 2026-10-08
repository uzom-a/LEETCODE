from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        order = defaultdict(list)
        for str_ in strs:
            if "".join(sorted(str_)) in order:
                order["".join(sorted(str_))].append(str_)
            else:
                order["".join(sorted(str_))].append(str_)

        return [val for val in order.values()]
        