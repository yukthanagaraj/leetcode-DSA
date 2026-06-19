
class TimeMap:

    def __init__(self):
        self.store = {}

    def set(self, key, value, timestamp):
        if key not in self.store:
            self.store[key] = []
        
        self.store[key].append((timestamp, value))

    def get(self, key, timestamp):
        if key not in self.store:
            return ""

        arr = self.store[key]
        left = 0
        right = len(arr) - 1
        result = ""

        while left <= right:
            mid = (left + right) // 2

            if arr[mid][0] <= timestamp:
                result = arr[mid][1]
                left = mid + 1
            else:
                right = mid - 1

        return result