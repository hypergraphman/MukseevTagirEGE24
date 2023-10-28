from time import time
f = open('b.txt')
n = int(f.readline())
a = [int(x) for x in f.read().split()]

mx = -float('inf')
ans = None
now = time()
m = 120
b = [0] * m
for i in range(n):
    right = a[i]
    left = b[(m - right % m) % m]
    s = right + left
    if left > right and s % 120 == 0 and s > mx:
        mx = s
        ans = (left, right)
    b[right % m] = max(right, b[right % m])
print(mx)
print(ans)
