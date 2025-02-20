class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        d = {}
        count = 0

        for item in emails:
            local, domain = item.split("@")
            local = local.split('+')[0].replace('.', '') #the local part remove the periods
            item = local + '@' + domain
        

            if item not in d:
                d[item] = True
                count += 1
    
        return count    

        """
        Time Complexity: O(n * m )
        Space Complexity: O(n * m)
        """        

        
