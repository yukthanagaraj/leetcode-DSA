class Solution:
    def numSmallerByFrequency(self, queries, words):

        def freq(s):
            smallest = min(s)
            return s.count(smallest)

        wordFreq = [freq(w) for w in words]
        wordFreq.sort()

        ans = []
        n = len(wordFreq)

        for q in queries:
            f = freq(q)
            idx = bisect_right(wordFreq, f)
            ans.append(n - idx)

        return ans