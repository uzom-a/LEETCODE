class Solution:
    def busyStudent(self, startTime: List[int], endTime: List[int], queryTime: int) -> int:
        """
        U-Understand
        what NUMBER of students were working during querytime that is between starttime and endtime

        M-Match
        array

        P-Plan
        create a variable count
        iterate through both starttime and endtime as a tuple
        if startime greater than querytime and less than endtime increase count
        else continue the loop

        I-Implement
        look down below
        """

        count = 0
        for a, b in zip(startTime,endTime):
            if a <= queryTime and b >= queryTime:
                count += 1

        return count

        """
        R-Review

        E-Evaluate
        Time Complexity: O(n)
        Space Complexity: O(1)
        """
