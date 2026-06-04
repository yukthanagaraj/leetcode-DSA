class Solution:
    def evaluate(self, expression):

        def parse(expr):
            res = []
            bal = 0
            cur = []

            for ch in expr:
                if ch == ' ' and bal == 0:
                    if cur:
                        res.append(''.join(cur))
                        cur = []
                else:
                    if ch == '(':
                        bal += 1
                    elif ch == ')':
                        bal -= 1
                    cur.append(ch)

            if cur:
                res.append(''.join(cur))

            return res

        scope = {}

        def eval_expr(expr):
            # integer
            if expr[0] != '(':
                if expr[0] == '-' or expr[0].isdigit():
                    return int(expr)
                return scope[expr][-1]

            expr = expr[1:-1]
            parts = parse(expr)

            op = parts[0]

            if op == "add":
                return eval_expr(parts[1]) + eval_expr(parts[2])

            if op == "mult":
                return eval_expr(parts[1]) * eval_expr(parts[2])

            # let
            assigned = []

            for i in range(1, len(parts) - 1, 2):
                if i == len(parts) - 2:
                    break

                var = parts[i]
                val = eval_expr(parts[i + 1])

                if var not in scope:
                    scope[var] = []

                scope[var].append(val)
                assigned.append(var)

            result = eval_expr(parts[-1])

            for var in assigned:
                scope[var].pop()

            return result

        return eval_expr(expression)