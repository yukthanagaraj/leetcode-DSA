class Solution:
    def isValid(self, s):
        stack = []

        for ch in s:

            # opening brackets
            if ch == '(' or ch == '{' or ch == '[':
                stack.append(ch)

            # closing brackets
            else:
                if len(stack) == 0:
                    return False

                top = stack.pop()

                if ch == ')' and top != '(':
                    return False

                if ch == '}' and top != '{':
                    return False

                if ch == ']' and top != '[':
                    return False

        return len(stack) == 0
        