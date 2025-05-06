class NumArray:

    def __init__(self, nums: List[int]):
        self.prefix = [0]

        for num in nums:
            self.prefix.append(num + self.prefix[-1])

    def sumRange(self, left: int, right: int) -> int:
        return self.prefix[right + 1] - self.prefix[left] #prefix[right + 1] includes all values up to right, and prefix[left] removes the sum before left.


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)


"""Why does this work?

prefix[4] = jars 0 + 1 + 2 + 3

prefix[1] = jars 0

So subtracting them cancels out the beans from jar 0, and you’re left with jars 1, 2, 3.

TL;DR (7-year-old style):
You keep track of how many jellybeans are in all jars up to each point.
Then to find how many are between two jars, you just subtract and it’s like magic subtraction that skips the ones before!
"""
