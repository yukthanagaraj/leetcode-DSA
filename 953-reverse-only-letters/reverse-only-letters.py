class Solution:
    def reverseOnlyLetters(self, s):
        
        chars = list(s)
        left = 0
        right = len(chars) - 1

        while left < right:

            # Move left if not a letter
            if not chars[left].isalpha():
                left += 1

            # Move right if not a letter
            elif not chars[right].isalpha():
                right -= 1

            # Swap letters
            else:
                chars[left], chars[right] = chars[right], chars[left]
                left += 1
                right -= 1

        return "".join(chars)