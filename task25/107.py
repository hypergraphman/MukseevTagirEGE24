def divs(n):
    d = {1, n}
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            d.add(i)
            d.add(n // i)
    return sorted(d)


c = 0
mn = 10**10
ans = 0
for i in range(153732, 225675):
    a = divs(i)
    if len(a) == 4:
        c += 1
        if  a[2] - a[1] < mn:
            mn = a[2] - a[1]
            ans = i
print(c, ans)