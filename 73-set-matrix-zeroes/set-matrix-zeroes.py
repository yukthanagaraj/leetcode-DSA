class Solution(object):
    def setZeroes(self, matrix):
        rows, cols = len(matrix), len(matrix[0])
        first_row_zero = any(matrix[0][j] == 0 for j in range(cols))
        first_col_zero = any(matrix[i][0] == 0 for i in range(rows))

        # Step 1: Use first row/col as markers
        for i in range(1, rows):
            for j in range(1, cols):
                if matrix[i][j] == 0:
                    matrix[i][0] = 0
                    matrix[0][j] = 0

        # Step 2: Zero out cells based on markers
        for i in range(1, rows):
            for j in range(1, cols):
                if matrix[i][0] == 0 or matrix[0][j] == 0:
                    matrix[i][j] = 0

        # Step 3: Handle first row and column separately
        if first_row_zero:
            for j in range(cols):
                matrix[0][j] = 0

        if first_col_zero:
            for i in range(rows):
                matrix[i][0] = 0
        