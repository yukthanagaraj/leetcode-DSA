from collections import defaultdict

class Solution:
    def countOfAtoms(self, formula):
        n = len(formula)
        stack = [defaultdict(int)]
        i = 0

        while i < n:
            if formula[i] == '(':
                stack.append(defaultdict(int))
                i += 1

            elif formula[i] == ')':
                i += 1

                start = i
                while i < n and formula[i].isdigit():
                    i += 1

                mult = int(formula[start:i] or "1")

                top = stack.pop()

                for atom, cnt in top.items():
                    stack[-1][atom] += cnt * mult

            else:
                start = i
                i += 1

                while i < n and formula[i].islower():
                    i += 1

                atom = formula[start:i]

                start = i
                while i < n and formula[i].isdigit():
                    i += 1

                cnt = int(formula[start:i] or "1")

                stack[-1][atom] += cnt

        atoms = sorted(stack[-1].items())

        res = []

        for atom, cnt in atoms:
            res.append(atom)
            if cnt > 1:
                res.append(str(cnt))

        return "".join(res)