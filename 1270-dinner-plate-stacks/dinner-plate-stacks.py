
class DinnerPlates:

    def __init__(self, capacity):
        self.capacity = capacity
        self.stacks = []
        self.available = []          # min-heap of stacks with space
        self.rightmost = -1

    def push(self, val):

        while self.available:
            idx = self.available[0]
            if idx >= len(self.stacks) or len(self.stacks[idx]) == self.capacity:
                heappop(self.available)
            else:
                break

        if not self.available:
            self.stacks.append([])
            idx = len(self.stacks) - 1
        else:
            idx = heappop(self.available)

        self.stacks[idx].append(val)

        if len(self.stacks[idx]) < self.capacity:
            heappush(self.available, idx)

        self.rightmost = max(self.rightmost, idx)

    def pop(self):

        while self.rightmost >= 0 and not self.stacks[self.rightmost]:
            self.rightmost -= 1

        if self.rightmost == -1:
            return -1

        val = self.stacks[self.rightmost].pop()

        heappush(self.available, self.rightmost)

        while self.stacks and not self.stacks[-1]:
            self.stacks.pop()

        self.rightmost = len(self.stacks) - 1

        return val

    def popAtStack(self, index):

        if index >= len(self.stacks) or not self.stacks[index]:
            return -1

        val = self.stacks[index].pop()

        heappush(self.available, index)

        while self.stacks and not self.stacks[-1]:
            self.stacks.pop()

        self.rightmost = len(self.stacks) - 1

        return val