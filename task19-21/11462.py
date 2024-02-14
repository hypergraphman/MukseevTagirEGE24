def f(x, y, c, m):
    if x**2 + y**2 >= 169:
        return c % 2 == m % 2
    if c >= m:
        return False
    moves = [f(x + 3, y, c + 1, m),
             f(x, y + 3, c + 1, m),
             f(x, y + 4, c + 1, m)]
    return any(moves) if (c + 1) % 2 == m % 2 else all(moves)


for s in range(1, 12 + 1):
    for m in range(1, 4 + 1):
        if f(s, 2, 0, m):
            print(s, m)
            break