import random

class Solution:

    def __init__(self, n, blacklist):
        self.bound = n - len(blacklist)
        self.mapping = {}

        black = set(blacklist)
        last = self.bound

        for b in blacklist:
            if b < self.bound:
                while last in black:
                    last += 1
                self.mapping[b] = last
                last += 1

    def pick(self):
        x = random.randint(0, self.bound - 1)
        return self.mapping.get(x, x)