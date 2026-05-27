
class Solution:
    def calcEquation(self, equations, values, queries):

        # build graph
        graph = defaultdict(list)

        for (a, b), val in zip(equations, values):
            graph[a].append((b, val))
            graph[b].append((a, 1 / val))

        # DFS function
        def dfs(src, target, visited):

            if src not in graph or target not in graph:
                return -1.0

            if src == target:
                return 1.0

            visited.add(src)

            for neighbor, value in graph[src]:

                if neighbor in visited:
                    continue

                result = dfs(neighbor, target, visited)

                if result != -1.0:
                    return value * result

            return -1.0

        # answer queries
        ans = []

        for src, target in queries:
            ans.append(dfs(src, target, set()))

        return ans