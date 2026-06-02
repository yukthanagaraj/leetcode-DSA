class Solution:
    def isValid(self, code):
        stack = []
        i = 0
        n = len(code)

        while i < n:
            if i > 0 and not stack:
                return False

            if code.startswith("<![CDATA[", i):
                if not stack:
                    return False

                j = code.find("]]>", i)
                if j == -1:
                    return False

                i = j + 3

            elif code.startswith("</", i):
                j = code.find(">", i)
                if j == -1:
                    return False

                tag = code[i + 2:j]

                if (
                    len(tag) < 1
                    or len(tag) > 9
                    or not tag.isalpha()
                    or not tag.isupper()
                ):
                    return False

                if not stack or stack[-1] != tag:
                    return False

                stack.pop()
                i = j + 1

            elif code[i] == "<":
                j = code.find(">", i)
                if j == -1:
                    return False

                tag = code[i + 1:j]

                if (
                    len(tag) < 1
                    or len(tag) > 9
                    or not tag.isalpha()
                    or not tag.isupper()
                ):
                    return False

                stack.append(tag)
                i = j + 1

            else:
                if not stack:
                    return False
                i += 1

        return len(stack) == 0