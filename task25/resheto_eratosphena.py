a = [True] * (20000 + 1)
a[0] = a[1] = False

for i in range(2, int(len(a) ** 0.5) + 1):
    if a[i]:
        for j in range(i ** 2, len(a), i):
            a[j] = False

primes = {i for i in range(len(a)) if a[i]}
print(len(primes))
