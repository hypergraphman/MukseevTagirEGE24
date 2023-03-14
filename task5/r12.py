def f(n):
    d1, d2, d3 = n // 100, n // 10 % 10, n % 10
    a = [d1 * 10 + d2, d2 * 10 + d1,
         d3 * 10 + d2, d2 * 10 + d3,
         d1 * 10 + d3, d3 * 10 + d1]
    # b = list(filter(lambda x: 10 <= x <= 99, a))
    b = []
    for el in a:
        if 10 <= el <= 99:
            b.append(el)
    return max(b) - min(b)


print(f(351))
i = 100
while f(i) != 40:
    i += 1
print(i)