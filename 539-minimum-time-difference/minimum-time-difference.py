class Solution:
    def findMinDifference(self, timePoints):
        minutes = []

        for time in timePoints:
            hour, minute = map(int, time.split(":"))
            total = hour * 60 + minute
            minutes.append(total)

        minutes.sort()

        minimum = float("inf")

        # Difference between consecutive times
        for i in range(1, len(minutes)):
            minimum = min(minimum, minutes[i] - minutes[i - 1])

        # Difference across midnight
        minimum = min(
            minimum,
            1440 - minutes[-1] + minutes[0]
        )

        return minimum