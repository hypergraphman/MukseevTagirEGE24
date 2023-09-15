f = open('26_225.txt')
# f = open('26_225_test.txt')
v, n = map(int, f.readline().split())
a = []
for el in f:
    a.append(int(el))
a.sort(reverse=True)

k = 0
last = None
for el in a:
    if v - el >= 0:
        last = el
        v -= el
        k += 1
print(k, last)


