class Solution:
    def canReach(self, arr, start):

        visited = set()

        def dfs(i):

            # out of bound or already visited
            if i < 0 or i >= len(arr) or i in visited:
                return False

            # reached value 0
            if arr[i] == 0:
                return True

            visited.add(i)

            # jump forward or backward
            return dfs(i + arr[i]) or dfs(i - arr[i])

        return dfs(start)
        