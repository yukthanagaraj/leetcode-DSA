class Solution(object):
    def evalRPN(self, tokens):
        """
        :type tokens: List[str]
        :rtype: int
        """

        stack = []

        for token in tokens:

            if token == "+":
                b = stack.pop()
                a = stack.pop()
                stack.append(a + b)

            elif token == "-":
                b = stack.pop()
                a = stack.pop()
                stack.append(a - b)

            elif token == "*":
                b = stack.pop()
                a = stack.pop()
                stack.append(a * b)

            elif token == "/":
                b = stack.pop()
                a = stack.pop()

                # truncate toward zero
                stack.append(int(float(a) / b))

            else:
                stack.append(int(token))

        return stack[0]