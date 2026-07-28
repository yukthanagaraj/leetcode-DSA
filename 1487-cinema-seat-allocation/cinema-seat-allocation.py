class Solution(object):
    def maxNumberOfFamilies(self, n, reservedSeats):
        """
        :type n: int
        :type reservedSeats: List[List[int]]
        :rtype: int
        """
        rows = {}

        # Store reserved seats for each row as a bitmask
        for r, s in reservedSeats:
            if r not in rows:
                rows[r] = 0
            rows[r] |= (1 << s)

        # Rows with no reserved seats can seat 2 groups
        ans = (n - len(rows)) * 2

        for mask in rows.values():
            left = (mask & ((1 << 2) | (1 << 3) | (1 << 4) | (1 << 5))) == 0
            middle = (mask & ((1 << 4) | (1 << 5) | (1 << 6) | (1 << 7))) == 0
            right = (mask & ((1 << 6) | (1 << 7) | (1 << 8) | (1 << 9))) == 0

            if left and right:
                ans += 2
            elif left or middle or right:
                ans += 1

        return ans