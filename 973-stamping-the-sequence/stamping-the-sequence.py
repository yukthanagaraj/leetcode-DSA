class Solution:
    def movesToStamp(self, stamp, target):
        n = len(target)
        m = len(stamp)

        target = list(target)
        result = []
        visited = [False] * (n - m + 1)

        def can_replace(pos):
            changed = False

            for i in range(m):
                if target[pos + i] != '?':
                    if target[pos + i] != stamp[i]:
                        return False
                    changed = True

            return changed

        def do_replace(pos):
            count = 0

            for i in range(m):
                if target[pos + i] != '?':
                    target[pos + i] = '?'
                    count += 1

            return count

        remaining = n

        while remaining > 0:
            found = False

            for i in range(n - m + 1):
                if not visited[i] and can_replace(i):
                    visited[i] = True

                    removed = do_replace(i)

                    if removed:
                        result.append(i)
                        remaining -= removed
                        found = True

            if not found:
                return []

        return result[::-1]
        