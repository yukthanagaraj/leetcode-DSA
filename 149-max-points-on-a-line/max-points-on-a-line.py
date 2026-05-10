class Solution(object):
    def maxPoints(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """

        n = len(points)

        if n <= 2:
            return n

        ans = 0

        for i in range(n):

            slopes = {}

            for j in range(i + 1, n):

                x1, y1 = points[i]
                x2, y2 = points[j]

                dx = x2 - x1
                dy = y2 - y1

                g = self.gcd(dx, dy)

                dx //= g
                dy //= g

                # normalize sign
                if dx < 0:
                    dx *= -1
                    dy *= -1

                # vertical line handling
                if dx == 0:
                    dy = 1

                # horizontal line handling
                if dy == 0:
                    dx = 1

                slope = (dy, dx)

                slopes[slope] = slopes.get(slope, 0) + 1

            current_max = 0

            for count in slopes.values():
                current_max = max(current_max, count)

            ans = max(ans, current_max + 1)

        return ans

    def gcd(self, a, b):

        while b:
            a, b = b, a % b

        return abs(a)
        