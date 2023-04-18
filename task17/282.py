*a, = map(int, open('17-282.txt'))

# min_17 = float('inf')
# for el in a:
#     if el % 17 == 0 and el < min_17:
#         min_17 = el

# k = 0
# mx = 0
# for i in range(1, len(a)):
#     p1, p2 = a[i - 1], a[i]
#     if p1 % 17 == 0 or p2 % 17 == 0:
#         k += 1
#         mx = max(p1 + p2, mx)
# print(k, mx)

min_17 = min(filter(lambda x: x % 17 == 0, a))

res = []
for p1, p2 in zip(a, a[1:]):
    if p1 % 17 == 0 or p2 % 17 == 0:
        res.append(p1 + p2)
print(len(res), min(res))