class Solution:
    def minDeletionSize(self, strs):
        n = len(strs)
        m = len(strs[0])
        
        ans = 0
        
        # adjacent pairs already confirmed sorted
        sorted_pair = [False] * (n - 1)
        
        for col in range(m):
            delete = False
            
            # Check if this column breaks any unsolved pair
            for row in range(n - 1):
                if not sorted_pair[row] and strs[row][col] > strs[row + 1][col]:
                    delete = True
                    break
            
            if delete:
                ans += 1
                continue
            
            # This column is kept, update solved pairs
            for row in range(n - 1):
                if strs[row][col] < strs[row + 1][col]:
                    sorted_pair[row] = True
        
        return ans