class Solution(object):
    def combinationSum(self, candidates, target):
        candidates.sort()
        result = []

        def backtrack(start, current, total):
            if total == target:
                result.append(list(current))
                return
            
            for i in range(start, len(candidates)):
                if total + candidates[i] > target:
                    break
                
                current.append(candidates[i])
                backtrack(i, current, total + candidates[i])
                current.pop()

        backtrack(0, [], 0)
        return result