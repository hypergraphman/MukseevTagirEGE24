# a = [0] * 27
# a[2] = 1
# for i in range(3, 27):
#     if i % 2 == 0 and (i > 10 and i // 2 >= 10 or i <= 10):
#         a[i] += a[i // 2]
#     if i != 19:
#         a[i] += a[i - 1]
# print(a)

# a = [0] * 52
# a[2] = 1
# for i in range(2, 10):
#     a[i + 1] += a[i]
#     if i * 2 <= 10:
#         a[i * 2] += a[i]
# for i in range(10, 26):
#     if i + 1 != 19:
#         a[i + 1] += a[i]
#     a[i * 2] += a[i]
# print(a[26])

def f(s, e):
    if s > e or s == 19:
        return 0
    if s == e:
        return 1
    return f(s + 1, e) + f(s * 2, e)

print(f(2, 10) * f(10, 26))