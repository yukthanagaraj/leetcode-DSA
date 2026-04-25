class Solution(object):
    def uniquePathsWithObstacles(self, obstacleGrid):
        """
        :type obstacleGrid: List[List[int]]
        :rtype: int
        """
        m, n = len(obstacleGrid), len(obstacleGrid[0])
        
        # If start or end is blocked, no paths exist
        if obstacleGrid[0][0] == 1 or obstacleGrid[m-1][n-1] == 1:
            return 0
        
        dp = [[0] * n for _ in range(m)]
        dp[0][0] = 1
        
        # Fill first column (stop if obstacle hit)
        for row in range(1, m):
            dp[row][0] = 0 if obstacleGrid[row][0] == 1 else dp[row-1][0]
        
        # Fill first row (stop if obstacle hit)
        for col in range(1, n):
            dp[0][col] = 0 if obstacleGrid[0][col] == 1 else dp[0][col-1]
        
        # Fill rest of the grid
        for row in range(1, m):
            for col in range(1, n):
                if obstacleGrid[row][col] == 1:
                    dp[row][col] = 0
                else:
                    dp[row][col] = dp[row-1][col] + dp[row][col-1]
        
        return dp[m-1][n-1]