class Solution(object):
    def checkValid(self, matrix):
        n = len(matrix)
        for r in range(n):
            row = bytearray(n + 1) 
            col = bytearray(n + 1) 
            for c in range(n):
                ro, co = matrix[r][c], matrix[c][r]
                row[ro] += 1
                col[co] += 1
                if row[ro] > 1 or col[co] > 1:
                    return False
        return True
        