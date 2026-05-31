

class Solution:
    def frequencySort(self, s):
        freq = Counter(s)

        return ''.join(
            ch * count
            for ch, count in sorted(freq.items(), key=lambda x: x[1], reverse=True)
        )