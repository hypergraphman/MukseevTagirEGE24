a = set()


def f(n, limit):
    if limit == 12:
        a.add(n)
        return
    f(n + 1, limit + 1)
    f(n * 2 - 3, limit + 1)


f(3, 0)
print(*sorted(a))

