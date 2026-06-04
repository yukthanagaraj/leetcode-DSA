from collections import defaultdict

class Solution:
    def accountsMerge(self, accounts):
        n = len(accounts)
        parent = list(range(n))

        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]

        def union(x, y):
            parent[find(x)] = find(y)

        email_to_account = {}

        for i, account in enumerate(accounts):
            for email in account[1:]:
                if email in email_to_account:
                    union(i, email_to_account[email])
                else:
                    email_to_account[email] = i

        groups = defaultdict(set)

        for email, idx in email_to_account.items():
            root = find(idx)
            groups[root].add(email)

        res = []

        for root, emails in groups.items():
            name = accounts[root][0]
            res.append([name] + sorted(emails))

        return res