class Solution:
    def reverseWords(self, s):
        words = s.split()
        
        for i in range(len(words)):
            words[i] = "".join(reversed(words[i]))
            
        return " ".join(words)