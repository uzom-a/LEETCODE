class Solution:
    def findLucky(self, arr: List[int]) -> int:
        """
        PSEUDOCODE
        -assign maxx to float('-inf')
        -use a counter to get the freq of the integers
        -iterate through that dictionary and check when key is equal to value
        -if yes, check if greater than th emaxx and store maxx
        -return max if maxx != float('-inf') else -1
        """

        maxx = float('-inf')

        count = Counter(arr)

        for key, value in count.items():
            if key == value:
                maxx = max(maxx, key)

        return maxx if maxx != float('-inf') else -1