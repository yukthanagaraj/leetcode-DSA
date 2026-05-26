class Solution:
    def check(self, num, a, b, start):
        if start == len(num):
            return True

        s = str(a + b)

        if not num.startswith(s, start):
            return False

        return self.check(num, b, a + b, start + len(s))

    def isAdditiveNumber(self, num):
        n = len(num)

        for i in range(1, n // 2 + 1):
            for j in range(1, n - i):

                # remaining length check
                if max(i, j) > n - i - j:
                    break

                # leading zero check
                if (num[0] == '0' and i > 1) or \
                   (num[i] == '0' and j > 1):
                    continue

                a = int(num[:i])
                b = int(num[i:i + j])

                if self.check(num, a, b, i + j):
                    return True

        return False