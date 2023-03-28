def n_to_p(n, p):
    res = ''
    d = '0123456789ABCDEF'
    while n > 0:
        res = d[n % p] + res
        n //= p
    return res


print(n_to_p(4 * 25 ** 2022 - 2 * 5 ** 2000 + 125 ** 1011 - 3 * 5 ** 100 - 600, 5).count('4'))
