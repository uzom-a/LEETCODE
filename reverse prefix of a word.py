class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        i = word.find(ch)
        cut_out = word[0:i+1] 
        reverse = cut_out[::-1]

        ans = reverse + word[i+1:]

        return ans

#the time complexity is ass tho O(n^2) isn't good
        
#THE CODE BELOW HAS A MORE OPTIMAL TIME COMPLEXITY WHICH IS O(N)

def reverse_until_char(word, ch):
    # Find the index of the character
    i = word.find(ch)
    
    # Create a list to store the result
    result = []
    
    # Reverse the part of the string up to and including `ch`
    for j in range(i + 1):
        result.append(word[i - j])  # Add characters in reverse order
    
    # Append the remaining part of the string after `ch`
    result.append(word[i + 1:])
    
    # Join the list to form the final string and return it
    return ''.join(result)
