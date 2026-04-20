class Solution(object):
    def solveSudoku(self, board):
        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        boxes = [set() for _ in range(9)]
        empty = []

        # Initialize constraint sets and collect empty cells
        for r in range(9):
            for c in range(9):
                val = board[r][c]
                if val == '.':
                    empty.append((r, c))
                else:
                    box = (r // 3) * 3 + c // 3
                    rows[r].add(val)
                    cols[c].add(val)
                    boxes[box].add(val)

        def backtrack(idx):
            if idx == len(empty):
                return True

            r, c = empty[idx]
            box = (r // 3) * 3 + c // 3

            for num in "123456789":
                if num not in rows[r] and num not in cols[c] and num not in boxes[box]:
                    # Place
                    board[r][c] = num
                    rows[r].add(num)
                    cols[c].add(num)
                    boxes[box].add(num)

                    if backtrack(idx + 1):
                        return True

                    # Undo
                    board[r][c] = '.'
                    rows[r].remove(num)
                    cols[c].remove(num)
                    boxes[box].remove(num)

            return False

        backtrack(0)
        