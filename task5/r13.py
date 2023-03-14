def f(n):
    # s1 = f'{n:b}'
    s1 = bin(n)[2:]
    s2 = s1 + str(s1.count('1') % 2)
    s3 = s2 + str(s2.count('1') % 2)
    return int(s3, 2)


print(f(28))
i = 1
while f(i) <= 77:
    i += 1
print(i)