for x in range(17):
    n = 1 * 17 ** 4 + 3 * 17 ** 3 + 5 * 17 ** 2 + x * 17 + 9 + 9 * 17 ** 4 + x * 17 ** 3 + 5 * 17 ** 2 + 3 * 17 + 1
    if n % 9 == 0:
        print(n // 9)
