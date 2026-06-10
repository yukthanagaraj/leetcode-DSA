class Solution:
    def pushDominoes(self, dominoes):
        
        dominoes = "L" + dominoes + "R"
        result = []
        prev = 0
        
        for i in range(1, len(dominoes)):
            
            if dominoes[i] == '.':
                continue
            
            middle = i - prev - 1
            
            if prev > 0:
                result.append(dominoes[prev])
            
            if dominoes[prev] == dominoes[i]:
                # Same direction
                result.append(dominoes[prev] * middle)
            
            elif dominoes[prev] == 'R' and dominoes[i] == 'L':
                # Moving towards each other
                result.append('R' * (middle // 2))
                
                if middle % 2 == 1:
                    result.append('.')
                
                result.append('L' * (middle // 2))
            
            else:
                # L...R stays same
                result.append('.' * middle)
            
            prev = i
        
        return ''.join(result)
        