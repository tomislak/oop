class Stock:
    def __init__(self, name, shares, price):
        self.name = name
        self.shares = shares
        self.price = price

    def cost(self):
        print(self.shares * self.price)

    def sell(self,shares):
        self.shares -= shares
