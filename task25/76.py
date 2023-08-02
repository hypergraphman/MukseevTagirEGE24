def divs(n):
    d = {1, n}
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            d.add(i)
            d.add(n // i)
    return (sorted(d))[:-1]


for i in range(2, 30_001):
    t = sum(divs(i))
    if i == sum(divs(t)) and i < t:
        print(i, t)