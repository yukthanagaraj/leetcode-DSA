class Solution(object):
    def maximalRectangle(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        if not matrix or not matrix[0]:
            return 0

        cols = len(matrix[0])
        heights = [0] * cols
        max_area = 0

        for row in matrix:
            # Build histogram heights
            for j in range(cols):
                heights[j] = heights[j] + 1 if row[j] == '1' else 0

            # Run largest rectangle in histogram
            max_area = max(max_area, self._largestRectangle(heights))

        return max_area

    def _largestRectangle(self, heights):
        stack = []
        max_area = 0

        for i, h in enumerate(heights):
            start = i
            while stack and stack[-1][1] > h:
                idx, height = stack.pop()
                max_area = max(max_area, height * (i - idx))
                start = idx
            stack.append((start, h))

        for idx, height in stack:
            max_area = max(max_area, height * (len(heights) - idx))

        return max_area