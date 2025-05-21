class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = defaultdict(int)
        res = []
        freq = [[] for i in range(len(nums)+1)] # so that we have indices for the max number of count since this is our bucket labelling for bucket sort

        for num in nums:
                count[num] += 1 #I don't need to do more than this since I used a default dict

        for num, c in count.items():
            freq[c].append(num)  #labelling the bucket plus putting numbers that get that freq in the correct label

        for i in range(len(freq) - 1, 0, -1):  #wee have to take the list from the back to get top k
            for value in freq[i]: #get into that toppost bucket
                res.append(value)
                if len(res) == k:
                    return res
