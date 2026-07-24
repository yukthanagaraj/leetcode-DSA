class Cashier:

    def __init__(self, n, discount, products, prices):
        self.n = n
        self.discount = discount
        self.count = 0
        self.price = {}

        for p, pr in zip(products, prices):
            self.price[p] = pr

    def getBill(self, product, amount):
        self.count += 1

        bill = 0
        for p, a in zip(product, amount):
            bill += self.price[p] * a

        if self.count % self.n == 0:
            bill = bill * (100 - self.discount) / 100.0

        return bill