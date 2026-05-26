class Solution:
    def removeDuplicateLetters(self, s):
        last_index = {ch: i for i, ch in enumerate(s)}
        
        stack = []
        visited = set()

        for i, ch in enumerate(s):

            if ch in visited:
                continue

            while stack and ch < stack[-1] and i < last_index[stack[-1]]:
                visited.remove(stack.pop())

            stack.append(ch)
            visited.add(ch)

        return "".join(stack)