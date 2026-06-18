from fractions import Fraction

class Solution:
    def isRationalEqual(self, s, t):

        def convert(x):

            if "." not in x:
                return Fraction(int(x), 1)

            integer, decimal = x.split(".")

            if "(" in decimal:
                non_rep, rep = decimal.split("(")
                rep = rep[:-1]
            else:
                non_rep = decimal
                rep = ""

            ans = Fraction(int(integer), 1)

            # non repeating part
            if non_rep:
                ans += Fraction(
                    int(non_rep),
                    10 ** len(non_rep)
                )

            # repeating part
            if rep:
                ans += Fraction(
                    int(rep),
                    (10 ** len(non_rep)) * (10 ** len(rep) - 1)
                )

            return ans

        return convert(s) == convert(t)