class Solution:
    def combinationSum3(self, k, n):

        result = []

        def backtrack(start, path, total):

            # Valid combination found
            if len(path) == k and total == n:
                result.append(path[:])
                return

            # Stop conditions
            if len(path) > k or total > n:
                return

            for num in range(start, 10):

                path.append(num)

                backtrack(num + 1, path, total + num)

                path.pop()

        backtrack(1, [], 0)

        return result
        