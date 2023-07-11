def divs(n):
    d = {1, n}
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            d.add(i)
            d.add(n // i)
        if len(d) > 3:
            break
    return sorted(d)


# print(divs(100))

for i in range(1000, 1414):
    a = divs(i)
    if len(a) == 2 and sum(map(int, str(i**2))) % 5 == 0:
        print(i**2, i)
print()

for i in range(1000000, 2000000):
    a = divs(i)
    if len(a) == 3 and sum(map(int, str(i))) % 5 == 0:
        print(i, a[1])

# 113569 337
# 139129 373
# 167281 409
# 175561 419
# 201601 449
# 214369 463
# 259081 509
# 358801 599
# 413449 643
# 426409 653
# 436921 661