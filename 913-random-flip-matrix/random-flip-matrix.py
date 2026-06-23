import random

class Solution:

    def __init__(self, m, n):
        self.m = m
        self.n = n
        self.total = m * n
        self.remaining = self.total
        self.map = {}

    def flip(self):
        # pick random index among remaining cells
        r = random.randint(0, self.remaining - 1)

        # get actual index
        x = self.map.get(r, r)

        # move last available position into r
        self.remaining -= 1
        self.map[r] = self.map.get(self.remaining, self.remaining)

        # convert 1D index to 2D
        return [x // self.n, x % self.n]

    def reset(self):
        self.remaining = self.total
        self.map.clear()