class Solution:
    def equationsPossible(self, equations):
        
        parent = [i for i in range(26)]

        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]

        def union(a, b):
            pa = find(a)
            pb = find(b)

            if pa != pb:
                parent[pb] = pa

        # Step 1: process equalities
        for eq in equations:
            if eq[1] == '=':
                a = ord(eq[0]) - ord('a')
                b = ord(eq[3]) - ord('a')
                union(a, b)

        # Step 2: check inequalities
        for eq in equations:
            if eq[1] == '!':
                a = ord(eq[0]) - ord('a')
                b = ord(eq[3]) - ord('a')

                if find(a) == find(b):
                    return False

        return True