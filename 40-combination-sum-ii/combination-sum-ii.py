class Solution(object):
    def combinationSum2(self, candidates, target):
        candidates.sort()
        result = []

        def backtrack(start, current, total):
            if total == target:
                result.append(list(current))
                return
            
            for i in range(start, len(candidates)):
                
                # 🚫 skip duplicates
                if i > start and candidates[i] == candidates[i - 1]:
                    continue
                
                # 🚫 pruning
                if total + candidates[i] > target:
                    break
                
                current.append(candidates[i])
                
                # i+1 → cannot reuse same element
                backtrack(i + 1, current, total + candidates[i])
                
                current.pop()
        
        backtrack(0, [], 0)
        return result