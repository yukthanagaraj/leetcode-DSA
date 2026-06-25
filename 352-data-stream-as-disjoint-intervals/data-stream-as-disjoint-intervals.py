import bisect

class SummaryRanges:

    def __init__(self):
        self.intervals = []

    def addNum(self, value):
        intervals = self.intervals

        # Find position to insert
        idx = bisect.bisect_left(intervals, [value, value])

        # Check if value is already covered by left interval
        if idx > 0 and intervals[idx - 1][0] <= value <= intervals[idx - 1][1]:
            return

        # Check if value is already covered by right interval
        if idx < len(intervals) and intervals[idx][0] == value:
            return

        # Merge with left and right intervals
        left_merge = idx > 0 and intervals[idx - 1][1] + 1 == value
        right_merge = idx < len(intervals) and intervals[idx][0] - 1 == value

        if left_merge and right_merge:
            intervals[idx - 1][1] = intervals[idx][1]
            intervals.pop(idx)

        elif left_merge:
            intervals[idx - 1][1] = value

        elif right_merge:
            intervals[idx][0] = value

        else:
            intervals.insert(idx, [value, value])

    def getIntervals(self):
        return self.intervals