from stock import Stock

a = Stock('GOOG', 100, 490.10)
b = Stock('APPL', 50, 122.34)
c = Stock('IBM', 75, 91.75)
stocks = [a, b, c]
for s in stocks:
    print(f'{s.name:>10s} {s.shares:>10d} {s.price:>10.2f}')

print(f'{a.name:>10s} {a.shares:>10d} {a.price:>10.2f}')

print(f'{a.name} cost {a.cost()}')

a.sell(25)

print(f'{a.name} cost {a.cost()}')

print(f'{a.name:>10s} {a.shares:>10d} {a.price:>10.2f}')
