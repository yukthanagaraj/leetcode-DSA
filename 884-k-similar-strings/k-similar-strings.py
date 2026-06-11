from collections import deque

class Solution:
    def kSimilarity(self, s1, s2):
        if s1 == s2:
            return 0

        q = deque([(s1, 0)])
        visited = {s1}

        while q:
            curr, steps = q.popleft()

            if curr == s2:
                return steps

            i = 0
            while curr[i] == s2[i]:
                i += 1

            curr_list = list(curr)

            for j in range(i + 1, len(curr)):
                if curr[j] == s2[i] and curr[j] != s2[j]:
                    nxt = curr_list[:]
                    nxt[i], nxt[j] = nxt[j], nxt[i]
                    nxt = ''.join(nxt)

                    if nxt not in visited:
                        visited.add(nxt)
                        q.append((nxt, steps + 1))