class Solution:
    def numSimilarGroups(self, strs):
        
        n = len(strs)
        visited = [False] * n
        
        def similar(a, b):
            diff = []
            
            for i in range(len(a)):
                if a[i] != b[i]:
                    diff.append(i)
            
            return len(diff) == 0 or (
                len(diff) == 2 and 
                a[diff[0]] == b[diff[1]] and 
                a[diff[1]] == b[diff[0]]
            )
        
        def dfs(i):
            visited[i] = True
            
            for j in range(n):
                if not visited[j] and similar(strs[i], strs[j]):
                    dfs(j)
        
        groups = 0
        
        for i in range(n):
            if not visited[i]:
                groups += 1
                dfs(i)
        
        return groups