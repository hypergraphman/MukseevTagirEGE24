from time import time
f = open('a.txt')
n = int(f.readline())
a = [int(x) for x in f.read().split()]
print(a)
mx = -float('inf')
ans = None
now = time()
for i in range(n - 1):
    for j in range(i + 1, n):
        s = a[i] + a[j]
        if a[i] > a[j] and s % 120 == 0 and s > mx:
            mx = s
            ans = (a[i], a[j])
    print(i, time() - now)
print(mx)
print(ans)