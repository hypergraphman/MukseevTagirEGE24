f = open('27-A_12257.txt')
n = int(f.readline())
a = [int(f.readline()) for i in range(n)]
# a = [int(x) for x in f]

k = 113
p = [(0, -1)] + [None] * (k - 1)
s = 0
res = (0, 0)
for i in range(len(a)):
    s += a[i]
    if p[s % k]:
        if s - p[s % k][0] > res[0]:
            res = (s - p[s % k][0], i - p[s % k][1])
        elif s - p[s % k][0] == res[0] and i - p[s % k][1] > res[1]:
            res = (s - p[s % k][0], i - p[s % k][1])
    else:
        p[s % k] = (s, i)
print(res)