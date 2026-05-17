class Solution:
    def generateParenthesis(self, n):
        result = []

        def backtrack(curr, open_count, close_count):

            # if length becomes 2*n
            if len(curr) == 2 * n:
                result.append(curr)
                return

            # add opening bracket
            if open_count < n:
                backtrack(curr + "(", open_count + 1, close_count)

            # add closing bracket
            if close_count < open_count:
                backtrack(curr + ")", open_count, close_count + 1)

        backtrack("", 0, 0)

        return result