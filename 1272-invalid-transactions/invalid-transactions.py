class Solution:
    def invalidTransactions(self, transactions):
        n = len(transactions)

        parsed = []
        for t in transactions:
            name, time, amount, city = t.split(',')
            parsed.append((name, int(time), int(amount), city))

        invalid = [False] * n

        # Rule 1: Amount > 1000
        for i in range(n):
            if parsed[i][2] > 1000:
                invalid[i] = True

        # Rule 2: Same name, different city, within 60 minutes
        for i in range(n):
            for j in range(i + 1, n):
                if (parsed[i][0] == parsed[j][0] and
                    parsed[i][3] != parsed[j][3] and
                    abs(parsed[i][1] - parsed[j][1]) <= 60):
                    invalid[i] = True
                    invalid[j] = True

        ans = []
        for i in range(n):
            if invalid[i]:
                ans.append(transactions[i])

        return ans