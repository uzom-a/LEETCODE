class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        output = set()

        for email in emails:
            before, after = email.split("@")
            if "+" in before:
                remaining, discard = before.split("+",1) #so that it only check the first plus sign

                cleaned = remaining.replace(".","")

                joined = cleaned +"@"+ after

                if joined not in output:
                    output.add(joined)

            else:
                cleaned = before.replace(".","")
                together = cleaned + "@" + after
                if together not in output:
                    output.add(together)
        return len(output)

        #Time Complexity and Space Complexity is O(n * k)