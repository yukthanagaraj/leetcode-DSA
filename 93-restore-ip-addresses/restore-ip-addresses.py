class Solution:
    def restoreIpAddresses(self,s):
        result = []

        def backtrack(start, path):

            # got 4 parts
            if len(path) == 4:

                # used all digits
                if start == len(s):
                    result.append(".".join(path))

                return

            # try 1 to 3 digits
            for i in range(1, 4):

                if start + i > len(s):
                    break

                part = s[start:start+i]

                # leading zero check
                if len(part) > 1 and part[0] == '0':
                    continue

                # range check
                if int(part) > 255:
                    continue

                backtrack(start + i, path + [part])

        backtrack(0, [])

        return result