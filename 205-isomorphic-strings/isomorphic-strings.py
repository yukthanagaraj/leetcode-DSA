class Solution:
    def isIsomorphic(self, s, t):
        mapST = {}
        mapTS = {}

        for c1, c2 in zip(s, t):

            # Check mapping from s -> t
            if c1 in mapST:
                if mapST[c1] != c2:
                    return False
            else:
                mapST[c1] = c2

            # Check mapping from t -> s
            if c2 in mapTS:
                if mapTS[c2] != c1:
                    return False
            else:
                mapTS[c2] = c1

        return True