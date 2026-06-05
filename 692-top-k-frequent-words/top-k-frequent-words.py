from collections import Counter

class Solution:
    def topKFrequent(self, words, k):
        count = Counter(words)

        return sorted(count.keys(), key=lambda w: (-count[w], w))[:k]