a = []
for n in range(87921, 88188):
    s = 0
    m = 1
    n = str(n)
    for i in range(len(n)):
        d = int(n[i])
        s += d
        m *= d

    if m != 0 and s % 14 == 0 and m % 18 == 0:
        a.append((m, s))
a.sort()
for m, s in a:
    print(s, m)