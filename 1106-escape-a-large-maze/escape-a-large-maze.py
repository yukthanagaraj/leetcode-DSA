from collections import deque
class Solution:
    def isEscapePossible(self, blocked, source, target):
        blocked = set(map(tuple, blocked))
        n = len(blocked)
        LIMIT = n * (n - 1) // 2

        def bfs(start, finish):
            q = deque([tuple(start)])
            visited = {tuple(start)}

            while q and len(visited) <= LIMIT:
                x, y = q.popleft()

                if (x, y) == tuple(finish):
                    return True

                for dx, dy in [(1,0),(-1,0),(0,1),(0,-1)]:
                    nx, ny = x + dx, y + dy

                    if (
                        0 <= nx < 10**6 and
                        0 <= ny < 10**6 and
                        (nx, ny) not in blocked and
                        (nx, ny) not in visited
                    ):
                        visited.add((nx, ny))
                        q.append((nx, ny))

            return len(visited) > LIMIT

        return bfs(source, target) and bfs(target, source)