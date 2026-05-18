class Solution:
    def lengthOfLastWord(self, s):
        # Remove spaces from start and end
        s = s.strip()

        # Split string into words
        words = s.split()

        # Return length of last word
        return len(words[-1])


# Example usage
obj = Solution()

print(obj.lengthOfLastWord("Hello World"))                  
print(obj.lengthOfLastWord("   fly me   to   the moon  "))  
print(obj.lengthOfLastWord("luffy is still joyboy"))        