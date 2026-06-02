class Solution:
    def checkInclusion(self, s1, s2):
        n1, n2 = len(s1), len(s2)

        if n1 > n2:
            return False

        cnt1 = [0] * 26
        cnt2 = [0] * 26

        for c in s1:
            cnt1[ord(c) - ord('a')] += 1

        for i in range(n1):
            cnt2[ord(s2[i]) - ord('a')] += 1

        if cnt1 == cnt2:
            return True

        for i in range(n1, n2):
            cnt2[ord(s2[i]) - ord('a')] += 1
            cnt2[ord(s2[i - n1]) - ord('a')] -= 1

            if cnt1 == cnt2:
                return True

        return False