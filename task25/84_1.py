a = []
for n in range(87921, 88188):
    s = 0
    m = 1
    f = True
    while n > 0:
        d = n % 10
        if d == 0:
            f = False
            break
        s += d
        m *= d
        n //= 10
    if f and s % 14 == 0 and m % 18 == 0:
        a.append((m, s))
a.sort()
for m, s in a:
    print(s, m)