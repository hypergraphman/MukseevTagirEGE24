f = open('26_11467.txt')
n = int(f.readline())
a = sorted([tuple(map(int, x.split())) for x in f], key=lambda x: x[1])
print(a[:10])
k = 1
nxt = a[0][1]
print(nxt)
for st, end in a:
    if st >= nxt:
        k += 1
        nxt = end
print(k)
