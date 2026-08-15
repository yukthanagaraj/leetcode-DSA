import heapq

class Solution:
    def reachableNodes(self, edges, maxMoves, n):

        # Build graph
        graph = [[] for _ in range(n)]

        for u, v, cnt in edges:
            graph[u].append((v, cnt))
            graph[v].append((u, cnt))

        # Shortest distance from node 0
        dist = [float('inf')] * n
        dist[0] = 0

        # Min heap: (distance, node)
        pq = [(0, 0)]

        while pq:

            d, u = heapq.heappop(pq)

            if d > dist[u]:
                continue

            for v, cnt in graph[u]:

                # Cost to reach the original node v
                new_dist = d + cnt + 1

                if new_dist < dist[v] and new_dist <= maxMoves:
                    dist[v] = new_dist
                    heapq.heappush(pq, (new_dist, v))

        # Count reachable original nodes
        answer = 0

        for d in dist:
            if d <= maxMoves:
                answer += 1

        # Count reachable subdivided nodes
        for u, v, cnt in edges:

            # How many subdivided nodes can we reach from u?
            from_u = maxMoves - dist[u] if dist[u] <= maxMoves else 0

            # How many can we reach from v?
            from_v = maxMoves - dist[v] if dist[v] <= maxMoves else 0

            # Can't exceed cnt
            answer += min(cnt, from_u + from_v)

        return answer