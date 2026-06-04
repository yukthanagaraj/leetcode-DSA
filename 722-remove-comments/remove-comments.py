class Solution:
    def removeComments(self, source):
        res = []
        in_block = False
        curr = []

        for line in source:
            i = 0

            if not in_block:
                curr = []

            while i < len(line):
                if not in_block and i + 1 < len(line) and line[i:i+2] == "/*":
                    in_block = True
                    i += 2

                elif in_block and i + 1 < len(line) and line[i:i+2] == "*/":
                    in_block = False
                    i += 2

                elif not in_block and i + 1 < len(line) and line[i:i+2] == "//":
                    break

                elif not in_block:
                    curr.append(line[i])
                    i += 1

                else:
                    i += 1

            if not in_block and curr:
                res.append("".join(curr))

        return res