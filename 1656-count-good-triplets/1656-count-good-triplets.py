class Solution:
    def countGoodTriplets(self, arr: List[int], a: int, b: int, c: int) -> int:
        #the largest number i snot to crazy for this brute force so let's goo
        count = 0
        for i in range(len(arr)):
            for j in range(i, len(arr)):
                for k in range(j, len(arr)):  #you should have used n instead of this len(arr) you are repeating like mad
                    if i != j and j != k and i != k:
                        if (abs(arr[i]-arr[j]) <= a) and (abs(arr[j]-arr[k]) <= b) and (abs(arr[i]-arr[k]) <= c):
                            count += 1

        return count

#Time Complexity: O(n)^3
#Space Complexity: O(1)