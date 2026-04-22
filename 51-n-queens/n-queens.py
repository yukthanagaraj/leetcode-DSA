class Solution(object):
    def solveNQueens(self, n):
        """
        :type n: int
        :rtype: List[List[str]]
        """
        results = []
        cols = set()
        diag1 = set()  # top-left to bottom-right (row - col)
        diag2 = set()  # top-right to bottom-left (row + col)

        def backtrack(row, board):
            if row == n:
                results.append(["".join(r) for r in board])
                return

            for col in range(n):
                if col in cols or (row - col) in diag1 or (row + col) in diag2:
                    continue

                cols.add(col)
                diag1.add(row - col)
                diag2.add(row + col)
                board[row][col] = "Q"

                backtrack(row + 1, board)

                cols.remove(col)
                diag1.remove(row - col)
                diag2.remove(row + col)
                board[row][col] = "."

        board = [["." for _ in range(n)] for _ in range(n)]
        backtrack(0, board)
        return results