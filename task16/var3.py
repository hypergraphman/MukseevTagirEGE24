from functools import lru_cache


@lru_cache(None)
def f(n):
    if n < 3:
        return 1
    if n > 2 and n % 2 != 0:
        return f(n - 1) + f(n - 2)
    return f(n - 1)


for i in range(1, 2400):
    f(i)


print(f(2400))