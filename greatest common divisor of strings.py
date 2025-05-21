class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        n, m = len(str1), len(str2)

        while m:
            n,m = m, n % m #this is the Eucladean method of finding the Greatest Common Divisor

        # Candidate substring of length n
        candidate = str1[:n]

        # Check if this substring divides both strings
        if str1 == candidate * (len(str1) // n) and str2 == candidate * (len(str2) // n):
            return candidate
        else:
            return ""

        
