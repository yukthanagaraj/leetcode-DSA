class Solution(object):
    def largestRectangleArea(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """
        stack = []  # stores indices
        max_area = 0
        
        for i, h in enumerate(heights):
            start = i
            while stack and stack[-1][1] > h:
                idx, height = stack.pop()
                max_area = max(max_area, height * (i - idx))
                start = idx  # extend left to where popped bar started
            stack.append((start, h))
        
        # Process remaining bars in stack (they extend to the end)
        for idx, height in stack:
            max_area = max(max_area, height * (len(heights) - idx))
        
        return max_area
        