from itertools import product

c = 0
for num in product('01234', repeat=3):
    if num[0] != '0' and num[0] >= num[1] >= num[2]:
        print(num)
        c += 1
print(c)