class Solution:
    def numberOfBoomerangs(self, points):
        ans = 0

        for i in range(len(points)):
            distance_map = {}

            for j in range(len(points)):
                if i == j:
                    continue

                dx = points[i][0] - points[j][0]
                dy = points[i][1] - points[j][1]

                dist = dx * dx + dy * dy

                distance_map[dist] = distance_map.get(dist, 0) + 1

            for count in distance_map.values():
                ans += count * (count - 1)

        return ans