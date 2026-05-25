class Solution:
    def removeInvalidParentheses(self, s):
        
        def isValid(string):
            count = 0
            
            for ch in string:
                if ch == '(':
                    count += 1
                elif ch == ')':
                    count -= 1
                    
                    if count < 0:
                        return False
                        
            return count == 0

        level = {s}

        while True:
            
            valid = []
            
            for string in level:
                if isValid(string):
                    valid.append(string)

            if valid:
                return valid

            next_level = set()

            for string in level:
                for i in range(len(string)):
                    
                    if string[i] not in '()':
                        continue

                    next_level.add(string[:i] + string[i+1:])

            level = next_level