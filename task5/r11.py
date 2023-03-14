def f(n):
    print(bin(n))
    s1 = bin(n)[2:]
    print(s1)
    s2 = s1[1:]
    print(s2)
    s3 = int(s2, 2)
    return n - s3


print(f(21))
s = set()
for i in range(500, 5000 + 1):
    s.add(f(i))
print(s)
print(len(s))