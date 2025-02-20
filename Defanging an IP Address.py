class Solution:
    def defangIPaddr(self, address: str) -> str:
        access = list(address)

        for i in range (len(access)):
            if access[i] == ".":
                access[i] = "[.]"

       
        return ''.join(access)

        "Time Complexity : O(n)"
        "Space Complexity: O(1)"
