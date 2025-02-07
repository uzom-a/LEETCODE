class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        seen = {}

        for num in nums:
            if num in seen:
                seen[num] += 1
            else:
                seen[num] = 1

        print(seen)
        for value in seen.values():
            if value >= 2:
                return True

        return False

    """
    U-Understand
    if you have more than one element in the array return True because well duh it contains a duplicate

    M-Match
    hashmap

    P-Plan
    create a hashmap
    loop through the array and count the occurence using the hashmap
    loop through the values of the array
    check if any value is at least 2
    if yes, return True
    else false

    I-Implement
    look above

    R-Review

    E-Evaluate
    Time Complexity: O(n)
    Space Complexity: O(n)
    """
