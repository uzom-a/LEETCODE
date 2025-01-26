class Solution:
    def compress(self, chars: List[str]) -> int:
        if len(chars) == 1:
            return 1

        first = 0
        write_index = 0  #necessary as we modify the array in-place

        for second in range(len(chars)):
            if second == len(chars) - 1 or chars[second] != chars[second + 1]: #if our second pointer is at the end of the array
                count = second - first + 1 #we need to increment second so that our count is accurate
                chars[write_index] = chars[first]
                write_index += 1
                
                if count > 1:
                    for digit in str(count): #incase the digit is greater than 10
                        chars[write_index] = digit
                        write_index += 1
                
                first = second + 1 #make our first start at the next unique character
        
        
        
        return write_index   #because whatever we are stopping
        """
        U-Understand:

        compress the string with the character and its count occurence then turn modify the OG list to represent the string character ad return the len

        M-Match: Array, two pointers
        P-Plan:
        iterate through the array with two pointers
        check if the second pointer is at the end of the consecutive repeating characters
        subtract second - first + 1 to get the length
        append the str of the length to the compressed string s
        at the end, convert s to a list and call the list chars

        I-Implement: look up

        R-Review:
        you are meant to modify the array in-place
        also, you need to check if the second pointer is already at the end before implementing count
        compare chars[second] with chars[second] + 1 to check for the new group of consecutives

        E-Evaluate
        Time Complexity: O(n) because that tiny for loop has a constraint of 2000 max
        Space Complexity : O(1)
        """

