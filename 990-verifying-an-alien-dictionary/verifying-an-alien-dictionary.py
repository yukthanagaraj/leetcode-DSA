class Solution:
    def isAlienSorted(self, words, order):
        
        # Store alien character order
        pos = {}
        for i, ch in enumerate(order):
            pos[ch] = i
        
        # Compare adjacent words
        for i in range(len(words) - 1):
            
            w1 = words[i]
            w2 = words[i + 1]
            
            length = min(len(w1), len(w2))
            found = False
            
            for j in range(length):
                
                if w1[j] != w2[j]:
                    if pos[w1[j]] > pos[w2[j]]:
                        return False
                    
                    found = True
                    break
            
            # If all characters matched, shorter word must come first
            if not found and len(w1) > len(w2):
                return False
        
        return True