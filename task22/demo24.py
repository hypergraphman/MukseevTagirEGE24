f = open('demo24.txt')
n = int(f.readline())
a = []
for i in range(n):
    x, y = map(int, f.readline().split())
    a.append(x)
    a.append(-y)
print(a)

a.sort(key=lambda x: abs(x))
print(a)

i_max_proc = 0
sum_max_proc = 0
count_proc = 0
for i in range(len(a)):
    if a[i] >= 0:
        count_proc += 1
